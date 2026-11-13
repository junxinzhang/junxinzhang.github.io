/**
 * Just Jason Hybrid CJK + English Search Engine
 * Zero-dependency BM25 + Exact Phrase + CJK Word/Bigram + Proximity Ranking
 * Supports progressive 2-tier full-text hydration, Traditional/Simplified Chinese,
 * contextual snippet highlighting, IME composition, and keyboard navigation.
 */
(function (root, factory) {
    if (typeof module !== 'undefined' && module.exports) {
        module.exports = factory();
    } else {
        root.JustJasonSearch = factory();
    }
})(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    // Verified 1-to-1 Traditional -> Simplified Chinese mapping for cross-script search
    var TRAD_CHARS = '離開廠實際踐專業發現動機會過對說為這來國經頭長見門間關電書車網絡點線買賣價錢費賬號規測評報圖標籤類題設備製計處決議項優準確錯難個們時後體學問雲運維構數據碼軟盤顯內儲寬帶節鏡庫視頻語識別譯轉寫讀聽講談論證驗試調誤監護欄權審風險隱鑰簽訂閱購續單銷營潤虧損資產負債創團隊員職崗辭簡歷晉績總黃勳偉達騰訊華蘋亞馬遜奧訓練餾參斂擬閉協許訴訟罰凍結復遷擴縮載遲丟併進鎖緩詢檢濾頁統儀組塊腳終變環誌蹤鏈斷異潰洩遞歸態靜編滾藍綠災雙櫃務戶瀏覽響應請狀衝區幣匯銀場廳醫療課認無與萬億從還讓給當將於並卻雖連繼隨種樣條層級階週趨勢戰啟邏輯壘紅槓桿複納爾糧鳥脫氾濫傳躍禮錶輪換鯨';
    var SIMP_CHARS = '离开厂实际践专业发现动机会过对说为这来国经头长见门间关电书车网络点线买卖价钱费账号规测评报图标签类题设备制计处决议项优准确错难个们时后体学问云运维构数据码软盘显内储宽带节镜库视频语识别译转写读听讲谈论证验试调误监护栏权审风险隐钥签订阅购续单销营润亏损资产负债创团队员职岗辞简历晋绩总黄勋伟达腾讯华苹亚马逊奥训练馏参敛拟闭协许诉讼罚冻结复迁扩缩载迟丢并进锁缓询检滤页统仪组块脚终变环志踪链断异溃泄递归态静编滚蓝绿灾双柜务户浏览响应请状冲区币汇银场厅医疗课认无与万亿从还让给当将于并却虽连继随种样条层级阶周趋势战启逻辑垒红杠杆复纳尔粮鸟脱泛滥传跃礼表轮换鲸';

    var TRAD_MAP = Object.create(null);
    for (var ti = 0; ti < TRAD_CHARS.length; ti++) {
        TRAD_MAP[TRAD_CHARS.charAt(ti)] = SIMP_CHARS.charAt(ti);
    }

    // Pure grammatical CJK particles ignored ONLY when isolated as 1-char tokens alongside real content terms
    var CJK_STOP_CHARS = Object.create(null);
    '的了着过吗呢吧啊呀哦哈与及或把被让给在有是我你他她它这那都也就而并但又很更最'.split('').forEach(function (ch) {
        CJK_STOP_CHARS[ch] = true;
    });

    var zhSegmenter = null;
    if (typeof Intl !== 'undefined' && typeof Intl.Segmenter === 'function') {
        try {
            zhSegmenter = new Intl.Segmenter('zh-CN', { granularity: 'word' });
        } catch (e) {
            zhSegmenter = null;
        }
    }

    var CJK_CHAR_RE = /[\u3400-\u9fff\uf900-\ufaff]/;
    var CJK_RUN_RE = /[\u3400-\u9fff\uf900-\ufaff]+/g;
    var ASCII_TOKEN_RE = /[a-z0-9]+(?:\.[0-9]+)*/g;

    function normChar(ch) {
        var c = ch.normalize ? ch.normalize('NFKC').toLowerCase() : ch.toLowerCase();
        if (c.length === 1 && TRAD_MAP[c]) {
            return TRAD_MAP[c];
        }
        return c;
    }

    function normalizeText(str) {
        if (!str) return '';
        var s = String(str);
        if (s.normalize) s = s.normalize('NFKC');
        s = s.toLowerCase();
        var out = '';
        for (var i = 0; i < s.length; i++) {
            var ch = s.charAt(i);
            out += TRAD_MAP[ch] || ch;
        }
        return out;
    }

    // Extract indexable tokens -> term frequency map (capped at 10 per field)
    function tokenizeForIndex(normStr) {
        var tf = Object.create(null);
        if (!normStr) return tf;

        function addTok(t) {
            if (!t) return;
            var cur = tf[t] || 0;
            if (cur < 10) tf[t] = cur + 1;
        }

        // 1. ASCII words & version numbers (e.g., "claude", "4.6", "grok4.6", "ocbc", "ai")
        var m;
        ASCII_TOKEN_RE.lastIndex = 0;
        while ((m = ASCII_TOKEN_RE.exec(normStr)) !== null) {
            var tok = m[0];
            addTok(tok);
            if (tok.indexOf('.') !== -1) {
                var parts = tok.split('.');
                for (var p = 0; p < parts.length; p++) {
                    if (parts[p].length >= 2) addTok(parts[p]);
                }
            }
        }

        // Also index hyphenated compounds without hyphen (e.g., "sd-wan" -> "sdwan", "grok-4.6" -> "grok4.6")
        var hyphRe = /[a-z0-9]+(?:-[a-z0-9.]+)+/g;
        while ((m = hyphRe.exec(normStr)) !== null) {
            addTok(m[0].replace(/-/g, ''));
        }

        // 2. CJK overlapping bigrams (blazing fast O(N) without ICU overhead on 1.5MB corpus)
        CJK_RUN_RE.lastIndex = 0;
        while ((m = CJK_RUN_RE.exec(normStr)) !== null) {
            var run = m[0];
            var len = run.length;
            if (len >= 2) {
                for (var i = 0; i < len - 1; i++) {
                    addTok(run.slice(i, i + 2));
                }
            }
        }

        return tf;
    }

    // Parse user query into structured clauses & atomic groups
    function parseQuery(rawQuery) {
        var qNorm = normalizeText(rawQuery).trim();
        if (!qNorm) return null;

        // Split into clauses by whitespace and punctuation (preserving dots inside digits like 4.6, and c++/c#)
        var rawClauses = qNorm
            .replace(/([0-9])\.([0-9])/g, '$1__DOT__$2')
            .split(/[\s,，.。:：;；!！?？、/\\|()（）【】\[\]《》<>「」『』“”"‘’'—\-–·~+*]+/)
            .map(function (c) { return c.replace(/__DOT__/g, '.').trim(); })
            .filter(Boolean);

        // Also detect special literal symbols like c++ or c#
        var specialLiterals = [];
        var specMatch = qNorm.match(/(?:c\+\+|c#|\.net)/g);
        if (specMatch) {
            for (var si = 0; si < specMatch.length; si++) {
                if (specialLiterals.indexOf(specMatch[si]) === -1) {
                    specialLiterals.push(specMatch[si]);
                }
            }
        }

        var groups = [];
        var highlightTerms = [];

        function pushHighlight(term) {
            if (term && highlightTerms.indexOf(term) === -1) {
                highlightTerms.push(term);
            }
        }

        for (var ci = 0; ci < rawClauses.length; ci++) {
            var clause = rawClauses[ci];
            pushHighlight(clause);

            // Split transitions between CJK and non-CJK
            var subRe = /[\u3400-\u9fff\uf900-\ufaff]+|[a-z0-9]+(?:\.[0-9]+)*/g;
            var sm;
            while ((sm = subRe.exec(clause)) !== null) {
                var sub = sm[0];
                if (CJK_CHAR_RE.test(sub.charAt(0))) {
                    var bigrams = [];
                    var segWords = [];
                    pushHighlight(sub);
                    if (sub.length >= 2) {
                        for (var bi = 0; bi < sub.length - 1; bi++) {
                            var bg = sub.slice(bi, bi + 2);
                            bigrams.push(bg);
                            pushHighlight(bg);
                        }
                        if (zhSegmenter) {
                            var segs = zhSegmenter.segment(sub);
                            for (var it = segs[Symbol.iterator](), st; !(st = it.next()).done;) {
                                var sw = st.value.segment;
                                if (sw.length >= 2) {
                                    segWords.push(sw);
                                    pushHighlight(sw);
                                }
                            }
                        }
                    }
                    groups.push({
                        type: 'cjk',
                        text: sub,
                        len: sub.length,
                        bigrams: bigrams,
                        segWords: segWords,
                        isStop: sub.length === 1 && !!CJK_STOP_CHARS[sub]
                    });
                } else {
                    pushHighlight(sub);
                    groups.push({
                        type: 'ascii',
                        text: sub,
                        len: sub.length,
                        isStop: false
                    });
                }
            }
        }

        // Filter out isolated 1-char CJK stopwords ONLY if there is at least one non-stop group
        var nonStopGroups = groups.filter(function (g) { return !g.isStop; });
        var effectiveGroups = nonStopGroups.length > 0 ? nonStopGroups : groups;

        // Sort highlight terms longest-first so full phrases highlight cleanly
        highlightTerms.sort(function (a, b) { return b.length - a.length; });

        return {
            raw: rawQuery,
            norm: qNorm,
            clauses: rawClauses,
            groups: effectiveGroups,
            specialLiterals: specialLiterals,
            highlightTerms: highlightTerms
        };
    }

    // Field configuration for BM25
    var FIELDS = [
        { name: 'title', weight: 16.0, b: 0.35 },
        { name: 'tags', weight: 10.5, b: 0.25 },
        { name: 'headings', weight: 7.5, b: 0.45 },
        { name: 'description', weight: 6.5, b: 0.50 },
        { name: 'slug', weight: 5.0, b: 0.20 },
        { name: 'faq', weight: 4.5, b: 0.55 },
        { name: 'body', weight: 1.6, b: 0.65 }
    ];
    var BM25_K1 = 1.2;

    function SearchEngine() {
        this.docs = [];
        this.docsByUrl = Object.create(null);
        // term -> Array of { d: docIdx, f: { fieldIdx: tf } }
        this.inverted = Object.create(null);
        this.asciiKeys = [];
        this.fieldAvgLen = new Float64Array(FIELDS.length);
        this.fieldTotals = new Float64Array(FIELDS.length);
        this.fulltextHydrated = false;
    }

    SearchEngine.prototype._extractSlug = function (url) {
        if (!url) return '';
        return String(url)
            .replace(/^https?:\/\/[^/]+/i, '')
            .replace(/\.html?$/i, '')
            .replace(/[^a-zA-Z0-9]+/g, ' ')
            .trim();
    };

    SearchEngine.prototype._prepareDoc = function (rawDoc, idx) {
        var url = rawDoc.url || rawDoc.id || '';
        var tagsArr = Array.isArray(rawDoc.tags) ? rawDoc.tags : [];
        var catsArr = Array.isArray(rawDoc.categories) ? rawDoc.categories : [];
        var combinedTags = catsArr.concat(tagsArr).join(' ');

        var title = rawDoc.title || '';
        var description = rawDoc.description || '';
        var headings = rawDoc.headings || '';
        var faq = rawDoc.faq || '';
        var body = rawDoc.body || '';
        var slug = this._extractSlug(url);

        var normFields = [
            normalizeText(title),
            normalizeText(combinedTags),
            normalizeText(headings),
            normalizeText(description),
            normalizeText(slug),
            normalizeText(faq),
            normalizeText(body)
        ];

        var fieldLens = new Int32Array(FIELDS.length);
        for (var fi = 0; fi < FIELDS.length; fi++) {
            fieldLens[fi] = Math.max(1, normFields[fi].length);
        }

        var dateTs = 0;
        if (rawDoc.date) {
            var parsedTs = Date.parse(rawDoc.date);
            if (!isNaN(parsedTs)) dateTs = parsedTs;
        }

        return {
            idx: idx,
            url: url,
            type: rawDoc.type || 'post',
            title: title,
            date: rawDoc.date || '',
            dateTs: dateTs,
            categories: catsArr,
            tags: tagsArr,
            description: description,
            headings: headings,
            faq: faq,
            body: body,
            normFields: normFields,
            fieldLens: fieldLens
        };
    };

    SearchEngine.prototype._indexDocFields = function (doc, fieldIndices) {
        var dIdx = doc.idx;
        for (var k = 0; k < fieldIndices.length; k++) {
            var fi = fieldIndices[k];
            var tfMap = tokenizeForIndex(doc.normFields[fi]);
            var terms = Object.keys(tfMap);
            for (var ti = 0; ti < terms.length; ti++) {
                var term = terms[ti];
                var postings = this.inverted[term];
                if (!postings) {
                    postings = [];
                    this.inverted[term] = postings;
                    if (/^[a-z0-9]/.test(term)) {
                        this.asciiKeys.push(term);
                    }
                }
                var last = postings.length > 0 ? postings[postings.length - 1] : null;
                if (last && last.d === dIdx) {
                    last.f[fi] = tfMap[term];
                } else {
                    var fObj = Object.create(null);
                    fObj[fi] = tfMap[term];
                    postings.push({ d: dIdx, f: fObj });
                }
            }
        }
    };

    SearchEngine.prototype._recomputeAvgLengths = function () {
        var n = Math.max(1, this.docs.length);
        for (var fi = 0; fi < FIELDS.length; fi++) {
            var sum = 0;
            for (var i = 0; i < this.docs.length; i++) {
                sum += this.docs[i].fieldLens[fi];
            }
            this.fieldTotals[fi] = sum;
            this.fieldAvgLen[fi] = Math.max(1, sum / n);
        }
        this.asciiKeys.sort();
    };

    // Synchronous build (fast enough for Node tests & <350 Tier-1 docs in ~8ms)
    SearchEngine.prototype.loadDocuments = function (rawDocs) {
        this.docs = [];
        this.docsByUrl = Object.create(null);
        this.inverted = Object.create(null);
        this.asciiKeys = [];
        this.fulltextHydrated = false;

        var allFields = [0, 1, 2, 3, 4, 5, 6];
        for (var i = 0; i < rawDocs.length; i++) {
            var r = rawDocs[i];
            if (!r || (!r.title && !r.body)) continue;
            var doc = this._prepareDoc(r, this.docs.length);
            this.docs.push(doc);
            if (doc.url) this.docsByUrl[doc.url] = doc;
            this._indexDocFields(doc, allFields);
        }
        this._recomputeAvgLengths();
    };

    // Hydrate Tier-2 full-text bodies (supports chunked async callback in browser or sync in Node)
    SearchEngine.prototype.hydrateFulltext = function (fulltextMap, onDone, asyncChunked) {
        if (!fulltextMap || typeof fulltextMap !== 'object') {
            this.fulltextHydrated = true;
            if (onDone) onDone();
            return;
        }

        var self = this;
        var urls = Object.keys(fulltextMap);
        for (var ui = 0; ui < urls.length; ui++) {
            var u = urls[ui];
            var doc = self.docsByUrl[u];
            if (!doc) continue;
            var fullBody = fulltextMap[u];
            if (!fullBody || fullBody.length <= doc.body.length) continue;
            doc.body = fullBody;
            doc.normFields[6] = normalizeText(fullBody);
            doc.fieldLens[6] = Math.max(1, doc.normFields[6].length);
        }

        // Rebuild clean inverted index in non-blocking chunks so df <= N is strictly preserved
        var nextInverted = Object.create(null);
        var nextAsciiKeys = [];
        var allFields = [0, 1, 2, 3, 4, 5, 6];
        var dCursor = 0;
        var chunkSize = asyncChunked ? 45 : self.docs.length + 1;

        function indexChunk() {
            var end = Math.min(dCursor + chunkSize, self.docs.length);
            for (var d = dCursor; d < end; d++) {
                var targetDoc = self.docs[d];
                for (var fi = 0; fi < allFields.length; fi++) {
                    var tfMap = tokenizeForIndex(targetDoc.normFields[fi]);
                    var terms = Object.keys(tfMap);
                    for (var ti = 0; ti < terms.length; ti++) {
                        var term = terms[ti];
                        var postings = nextInverted[term];
                        if (!postings) {
                            postings = [];
                            nextInverted[term] = postings;
                            if (/^[a-z0-9]/.test(term)) {
                                nextAsciiKeys.push(term);
                            }
                        }
                        var last = postings.length > 0 ? postings[postings.length - 1] : null;
                        if (last && last.d === d) {
                            last.f[fi] = tfMap[term];
                        } else {
                            var fObj = Object.create(null);
                            fObj[fi] = tfMap[term];
                            postings.push({ d: d, f: fObj });
                        }
                    }
                }
            }
            dCursor = end;
            if (dCursor < self.docs.length) {
                if (typeof requestIdleCallback === 'function') {
                    requestIdleCallback(indexChunk, { timeout: 120 });
                } else {
                    setTimeout(indexChunk, 0);
                }
            } else {
                self.inverted = nextInverted;
                self.asciiKeys = nextAsciiKeys;
                self._recomputeAvgLengths();
                self.fulltextHydrated = true;
                if (onDone) onDone();
            }
        }

        indexChunk();
    };

    SearchEngine.prototype._scoreTermPostings = function (term, scoreBuf, hitMask, bitFlag, weightMul) {
        var postings = this.inverted[term];
        if (!postings || postings.length === 0) return;

        var N = this.docs.length;
        var df = postings.length;
        if (df === 0) return;

        var idf = Math.max(0.08, Math.log(1 + (N - df + 0.5) / (df + 0.5)));
        for (var pi = 0; pi < postings.length; pi++) {
            var post = postings[pi];
            var dIdx = post.d;
            var doc = this.docs[dIdx];
            var fMap = post.f;
            var docTermScore = 0;
            var matchedAnyField = false;

            for (var fiStr in fMap) {
                var fi = Number(fiStr);
                var tf = fMap[fi];
                var fCfg = FIELDS[fi];
                var dl = doc.fieldLens[fi];
                var avgdl = this.fieldAvgLen[fi];
                var tfNorm = (tf * (BM25_K1 + 1)) / (tf + BM25_K1 * (1 - fCfg.b + fCfg.b * (dl / avgdl)));
                docTermScore += fCfg.weight * idf * tfNorm;
                matchedAnyField = true;
            }

            if (matchedAnyField) {
                scoreBuf[dIdx] += docTermScore * weightMul;
                if (hitMask && bitFlag) {
                    hitMask[dIdx] |= bitFlag;
                }
            }
        }
    };

    SearchEngine.prototype._findPrefixTerms = function (prefix) {
        var matches = [];
        // Binary search start in sorted asciiKeys
        var lo = 0, hi = this.asciiKeys.length - 1;
        while (lo <= hi) {
            var mid = (lo + hi) >>> 1;
            if (this.asciiKeys[mid] < prefix) lo = mid + 1;
            else hi = mid - 1;
        }
        for (var i = lo; i < this.asciiKeys.length && matches.length < 12; i++) {
            var k = this.asciiKeys[i];
            if (k.indexOf(prefix) === 0) {
                if (k !== prefix) matches.push(k);
            } else {
                break;
            }
        }
        return matches;
    };

    SearchEngine.prototype.search = function (rawQuery, options) {
        var opts = options || {};
        var limit = opts.limit || 30;
        var parsed = parseQuery(rawQuery);
        if (!parsed || this.docs.length === 0) return [];

        var N = this.docs.length;
        var groups = parsed.groups;
        var G = groups.length;

        var totalScore = new Float64Array(N);
        var groupHitCount = new Int16Array(N);
        var groupScoreBuf = new Float64Array(N);

        // 1. Evaluate each query group
        for (var gi = 0; gi < G; gi++) {
            var g = groups[gi];
            groupScoreBuf.fill(0);

            if (g.type === 'ascii') {
                // Exact token match
                this._scoreTermPostings(g.text, groupScoreBuf, null, 0, 1.25);

                // Prefix match ONLY for ASCII tokens of length >= 3
                if (g.len >= 3) {
                    var prefTerms = this._findPrefixTerms(g.text);
                    for (var pti = 0; pti < prefTerms.length; pti++) {
                        this._scoreTermPostings(prefTerms[pti], groupScoreBuf, null, 0, 0.70);
                    }
                }

                for (var di = 0; di < N; di++) {
                    if (groupScoreBuf[di] > 0) {
                        groupHitCount[di]++;
                        totalScore[di] += groupScoreBuf[di];
                    }
                }
            } else if (g.type === 'cjk') {
                if (g.len === 1) {
                    // Single CJK character direct scan across fields
                    var ch = g.text;
                    var df1 = 0;
                    for (var d0 = 0; d0 < N; d0++) {
                        var nf0 = this.docs[d0].normFields;
                        if (nf0[0].indexOf(ch) !== -1 || nf0[1].indexOf(ch) !== -1 || nf0[2].indexOf(ch) !== -1 || nf0[3].indexOf(ch) !== -1 || nf0[6].indexOf(ch) !== -1) {
                            df1++;
                        }
                    }
                    if (df1 > 0) {
                        var idf1 = Math.log(1 + (N - df1 + 0.5) / (df1 + 0.5));
                        for (var d1 = 0; d1 < N; d1++) {
                            var nf = this.docs[d1].normFields;
                            var s1 = 0;
                            for (var fi = 0; fi < FIELDS.length; fi++) {
                                if (nf[fi].indexOf(ch) !== -1) {
                                    s1 += FIELDS[fi].weight * idf1;
                                }
                            }
                            if (s1 > 0) {
                                groupHitCount[d1]++;
                                totalScore[d1] += s1;
                            }
                        }
                    }
                } else if (g.len === 2) {
                    // 2-char CJK word = exact single bigram
                    this._scoreTermPostings(g.text, groupScoreBuf, null, 0, 1.35);
                    for (var d2 = 0; d2 < N; d2++) {
                        if (groupScoreBuf[d2] > 0) {
                            groupHitCount[d2]++;
                            totalScore[d2] += groupScoreBuf[d2];
                        }
                    }
                } else {
                    // 3+ char CJK phrase: track per-bigram hits AND character coverage!
                    var bCount = g.bigrams.length; // <= 30 typically
                    var segWordSet = Object.create(null);
                    for (var swi = 0; swi < g.segWords.length; swi++) {
                        segWordSet[g.segWords[swi]] = true;
                    }

                    // Track character coverage per doc using a compact boolean/count array
                    // For bCount <= 30, a 32-bit bitmask of matched bigrams is blazing fast!
                    var useBitmask = bCount <= 30;
                    var bigramMask = useBitmask ? new Int32Array(N) : null;
                    var bigramHitCounts = useBitmask ? null : new Int16Array(N);

                    for (var bi = 0; bi < bCount; bi++) {
                        var bg = g.bigrams[bi];
                        var wMul = segWordSet[bg] ? 1.25 : 0.85;
                        if (useBitmask) {
                            this._scoreTermPostings(bg, groupScoreBuf, bigramMask, (1 << bi), wMul);
                        } else {
                            var tmpMask = new Int32Array(N);
                            this._scoreTermPostings(bg, groupScoreBuf, tmpMask, 1, wMul);
                            for (var dx = 0; dx < N; dx++) {
                                if (tmpMask[dx]) bigramHitCounts[dx]++;
                            }
                        }
                    }

                    for (var d3 = 0; d3 < N; d3++) {
                        if (groupScoreBuf[d3] <= 0) continue;

                        var charCovered = 0;
                        var bHits = 0;
                        if (useBitmask) {
                            var mask = bigramMask[d3];
                            if (mask === 0) continue;
                            var prevCovered = false;
                            for (var cPos = 0; cPos < g.len; cPos++) {
                                var leftHit = cPos > 0 && ((mask & (1 << (cPos - 1))) !== 0);
                                var rightHit = cPos < bCount && ((mask & (1 << cPos)) !== 0);
                                if (leftHit || rightHit) charCovered++;
                                if (rightHit) bHits++;
                            }
                        } else {
                            bHits = bigramHitCounts[d3];
                            charCovered = Math.min(g.len, bHits + 1);
                        }

                        var charRatio = charCovered / g.len;
                        var bigramRatio = bHits / bCount;

                        // Coverage threshold:
                        // L == 3 (e.g. "大模型", "黄仁勋", "黑皮衣"): require 2/2 bigrams = 100%
                        // L >= 4 (e.g. "才是靠近" -> "才是真正靠近"): require >= 75% char coverage!
                        var passedStrict = (g.len === 3) ? (bHits === bCount) : (charRatio >= 0.75);
                        if (passedStrict) {
                            groupHitCount[d3]++;
                            totalScore[d3] += groupScoreBuf[d3] * (0.65 + 0.35 * bigramRatio);
                        } else if (charRatio >= 0.55 && bHits >= 1) {
                            // Keep tiny partial credit ONLY in case 0 strict matches exist across corpus
                            totalScore[d3] += groupScoreBuf[d3] * 0.18 * charRatio;
                        }
                    }
                }
            }
        }

        // 2. Check special literals (e.g. c++, c#, .net)
        if (parsed.specialLiterals.length > 0) {
            for (var sli = 0; sli < parsed.specialLiterals.length; sli++) {
                var lit = parsed.specialLiterals[sli];
                for (var dl = 0; dl < N; dl++) {
                    var nfl = this.docs[dl].normFields;
                    if (nfl[0].indexOf(lit) !== -1) totalScore[dl] += 65;
                    else if (nfl[1].indexOf(lit) !== -1 || nfl[2].indexOf(lit) !== -1) totalScore[dl] += 40;
                    else if (nfl[6].indexOf(lit) !== -1) totalScore[dl] += 18;
                }
            }
        }

        // 3. Determine strict vs fallback candidates
        var strictCandidates = [];
        var fallbackCandidates = [];
        var minFallbackGroups = G >= 2 ? Math.max(1, Math.ceil(G * 0.65)) : 1;

        for (var d = 0; d < N; d++) {
            if (totalScore[d] <= 0) continue;
            if (G > 0 && groupHitCount[d] === G) {
                strictCandidates.push(d);
            } else if (groupHitCount[d] >= minFallbackGroups || (G === 1 && totalScore[d] > 8)) {
                fallbackCandidates.push(d);
            }
        }

        var candidateIndices = strictCandidates.length > 0 ? strictCandidates : fallbackCandidates;
        // If only 1-2 strict matches exist for a multi-group query (G >= 3), append top fallback candidates discounted
        if (strictCandidates.length > 0 && strictCandidates.length < 3 && G >= 3 && fallbackCandidates.length > 0) {
            for (var fi2 = 0; fi2 < fallbackCandidates.length; fi2++) {
                var fdIdx = fallbackCandidates[fi2];
                var covRatio = groupHitCount[fdIdx] / G;
                totalScore[fdIdx] *= (covRatio * covRatio * 0.45);
                candidateIndices.push(fdIdx);
            }
        }

        if (candidateIndices.length === 0) return [];

        // 4. Exact Phrase, Clause Substring, Order & Proximity Bonuses on Candidate Set
        var fullNorm = parsed.norm;
        var strippedNorm = fullNorm.replace(/[\s,，.。:：;；!！?？、/\\|()（）【】\[\]《》<>「」『』“”"‘’'—\-–·~]+/g, '');

        for (var ci2 = 0; ci2 < candidateIndices.length; ci2++) {
            var docIdx = candidateIndices[ci2];
            var doc = this.docs[docIdx];
            var nfDoc = doc.normFields;
            var bonus = 0;

            // 4a. Exact full query match in title / tags / headings / description / faq / body
            var isShortAsciiQuery = /^[a-z0-9]+$/.test(fullNorm) && fullNorm.length <= 3;
            if (fullNorm.length >= 2 && !isShortAsciiQuery) {
                var tIdx = nfDoc[0].indexOf(fullNorm);
                if (tIdx !== -1) {
                    bonus += 80;
                    if (tIdx === 0) bonus += 25;
                    if (nfDoc[0] === fullNorm) bonus += 40;
                }
                if (nfDoc[1].indexOf(fullNorm) !== -1) bonus += 45;
                if (nfDoc[2].indexOf(fullNorm) !== -1) bonus += 35;
                if (nfDoc[3].indexOf(fullNorm) !== -1) bonus += 28;
                if (nfDoc[5].indexOf(fullNorm) !== -1) bonus += 24;
                if (nfDoc[6].indexOf(fullNorm) !== -1) bonus += 18;
            }

            // Punctuation-stripped exact match (e.g., query "离开大厂，才是靠近" matching FAQ "离开大厂才是靠近")
            if (strippedNorm.length >= 3 && strippedNorm !== fullNorm) {
                var strippedTitle = nfDoc[0].replace(/[\s,，.。:：;；!！?？—\-–·]+/g, '');
                if (strippedTitle.indexOf(strippedNorm) !== -1) bonus += 65;
                if (nfDoc[5].indexOf(strippedNorm) !== -1) bonus += 28;
            }

            // 4b. Individual multi-char clause exact substring bonuses
            for (var cli = 0; cli < parsed.clauses.length; cli++) {
                var cl = parsed.clauses[cli];
                if (cl.length < 2) continue;
                // Avoid short ASCII false substring bonus inside longer ASCII words
                if (/^[a-z0-9]+$/.test(cl) && cl.length <= 3) continue;

                if (nfDoc[0].indexOf(cl) !== -1) bonus += 22 + Math.min(20, cl.length * 3);
                if (nfDoc[1].indexOf(cl) !== -1) bonus += 18;
                if (nfDoc[2].indexOf(cl) !== -1) bonus += 14;
                if (nfDoc[3].indexOf(cl) !== -1) bonus += 10;
                if (nfDoc[6].indexOf(cl) !== -1) bonus += 6;
            }

            // 4c. Ordered proximity bonus across highlight/group anchor terms in title & body
            if (groups.length >= 2 || (groups.length === 1 && groups[0].segWords && groups[0].segWords.length >= 2)) {
                var anchors = [];
                for (var ag = 0; ag < groups.length; ag++) {
                    var grp = groups[ag];
                    if (grp.type === 'cjk' && grp.segWords && grp.segWords.length >= 2) {
                        for (var asw = 0; asw < grp.segWords.length; asw++) anchors.push(grp.segWords[asw]);
                    } else {
                        anchors.push(grp.text);
                    }
                }
                if (anchors.length >= 2) {
                    bonus += this._computeOrderProximityBonus(nfDoc[0], anchors, 32, 35);
                    bonus += this._computeOrderProximityBonus(nfDoc[3], anchors, 48, 14);
                    bonus += this._computeOrderProximityBonus(nfDoc[6], anchors, 60, 10);
                }
            }

            // 4d. Subtle recency tie-breaker (up to +1.5 points for newer posts, never overriding real relevance)
            if (doc.dateTs > 0) {
                var yearsSince2020 = Math.max(0, (doc.dateTs - 1577836800000) / (365.25 * 86400000));
                bonus += Math.min(1.8, yearsSince2020 * 0.22);
            }

            totalScore[docIdx] += bonus;
        }

        // 5. Sort descending by final score
        candidateIndices.sort(function (a, b) {
            var diff = totalScore[b] - totalScore[a];
            if (Math.abs(diff) > 1e-6) return diff;
            return (this.docs[b].dateTs || 0) - (this.docs[a].dateTs || 0);
        }.bind(this));

        // Drop noisy tail results whose score is < 12% of top result score (when top score is strong)
        var topScore = totalScore[candidateIndices[0]];
        var minKeepScore = topScore > 60 ? topScore * 0.12 : 0;

        var results = [];
        for (var ri = 0; ri < candidateIndices.length && results.length < limit; ri++) {
            var rDocIdx = candidateIndices[ri];
            var rScore = totalScore[rDocIdx];
            if (ri > 0 && rScore < minKeepScore) break;
            var rDoc = this.docs[rDocIdx];
            results.push({
                doc: rDoc,
                score: rScore,
                titleHtml: buildHighlightedHtml(rDoc.title, parsed),
                snippetHtml: buildContextualSnippet(rDoc, parsed)
            });
        }

        return results;
    };

    SearchEngine.prototype._computeOrderProximityBonus = function (normField, anchors, maxSpan, maxBonus) {
        if (!normField || anchors.length < 2) return 0;
        var prevPos = -1;
        var firstPos = -1;
        var inOrderHits = 0;

        for (var i = 0; i < anchors.length; i++) {
            var a = anchors[i];
            if (!a) continue;
            var searchFrom = prevPos >= 0 ? prevPos : 0;
            var pos = normField.indexOf(a, searchFrom);
            if (pos === -1 && prevPos >= 0) {
                pos = normField.indexOf(a, 0);
            }
            if (pos !== -1) {
                if (firstPos === -1) firstPos = pos;
                if (pos >= prevPos) {
                    inOrderHits++;
                    prevPos = pos + a.length;
                }
            }
        }

        if (inOrderHits < 2) return 0;
        var span = prevPos - firstPos;
        if (span <= 0) return 0;
        var tightness = span <= maxSpan ? 1.0 : Math.max(0.2, maxSpan / span);
        return maxBonus * (inOrderHits / anchors.length) * tightness;
    };

    function escapeHtml(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function isAsciiAlnum(ch) {
        if (!ch) return false;
        var code = ch.charCodeAt(0);
        return (code >= 48 && code <= 57) || (code >= 97 && code <= 122);
    }

    // Map normalized match intervals accurately back to original text and wrap with <mark class="search-hl">
    function buildHighlightedHtml(origText, parsed) {
        if (!origText) return '';
        if (!parsed || !parsed.highlightTerms || parsed.highlightTerms.length === 0) {
            return escapeHtml(origText);
        }

        // Build normStr alongside origOffset mapping
        var normStr = '';
        var normToOrigStart = [];
        var normToOrigEnd = [];
        for (var i = 0; i < origText.length; i++) {
            var nc = normChar(origText.charAt(i));
            for (var k = 0; k < nc.length; k++) {
                normStr += nc.charAt(k);
                normToOrigStart.push(i);
                normToOrigEnd.push(i + 1);
            }
        }

        var intervals = [];
        var terms = parsed.highlightTerms;

        for (var ti = 0; ti < terms.length; ti++) {
            var term = terms[ti];
            if (!term) continue;
            // Skip highlighting isolated 1-char CJK stopwords unless query is 1 char
            if (term.length === 1 && CJK_STOP_CHARS[term] && parsed.norm.length > 1) continue;

            var isShortAscii = /^[a-z0-9]+$/.test(term) && term.length <= 2;
            var isLongerAscii = /^[a-z0-9]+$/.test(term) && term.length >= 3;

            var pos = 0;
            while (pos < normStr.length) {
                var idx = normStr.indexOf(term, pos);
                if (idx === -1) break;
                var endIdx = idx + term.length;

                var validBoundary = true;
                if (isShortAscii) {
                    var beforeCh = idx > 0 ? normStr.charAt(idx - 1) : '';
                    var afterCh = endIdx < normStr.length ? normStr.charAt(endIdx) : '';
                    if (isAsciiAlnum(beforeCh) || isAsciiAlnum(afterCh)) {
                        validBoundary = false;
                    }
                } else if (isLongerAscii) {
                    var beforeCh2 = idx > 0 ? normStr.charAt(idx - 1) : '';
                    if (isAsciiAlnum(beforeCh2)) {
                        validBoundary = false;
                    } else {
                        // Extend highlight to full word if prefix matched
                        while (endIdx < normStr.length && isAsciiAlnum(normStr.charAt(endIdx))) {
                            endIdx++;
                        }
                    }
                }

                if (validBoundary && idx < normToOrigStart.length) {
                    var oStart = normToOrigStart[idx];
                    var oEnd = normToOrigEnd[Math.min(endIdx - 1, normToOrigEnd.length - 1)];
                    intervals.push([oStart, oEnd]);
                }
                pos = idx + 1;
            }
        }

        if (intervals.length === 0) {
            return escapeHtml(origText);
        }

        // Sort & merge overlapping intervals
        intervals.sort(function (a, b) { return a[0] - b[0] || a[1] - b[1]; });
        var merged = [intervals[0]];
        for (var mi = 1; mi < intervals.length; mi++) {
            var prev = merged[merged.length - 1];
            var cur = intervals[mi];
            if (cur[0] <= prev[1]) {
                if (cur[1] > prev[1]) prev[1] = cur[1];
            } else {
                merged.push(cur);
            }
        }

        var html = '';
        var cursor = 0;
        for (var j = 0; j < merged.length; j++) {
            var s = merged[j][0];
            var e = merged[j][1];
            if (s > cursor) html += escapeHtml(origText.slice(cursor, s));
            html += '<mark class="search-hl">' + escapeHtml(origText.slice(s, e)) + '</mark>';
            cursor = e;
        }
        if (cursor < origText.length) {
            html += escapeHtml(origText.slice(cursor));
        }
        return html;
    }

    function stripOpeningBoilerplate(text) {
        if (!text) return '';
        return text
            .replace(/^\d{4}[/-]\d{2}[/-]\d{2}\s*-\s*/, '')
            .replace(/^大家好[，,\s]*我是\s*Jason[。.\s!！]*/i, '')
            .trim();
    }

    // Find best 145-char contextual snippet centered on matched terms
    function buildContextualSnippet(doc, parsed) {
        var cleanBody = stripOpeningBoilerplate(doc.body);
        var candidates = [
            { text: doc.description || '', bonus: 3.5 },
            { text: cleanBody, bonus: 1.5 },
            { text: doc.headings || '', bonus: 1.25 },
            { text: doc.faq || '', bonus: 1.15 }
        ];

        var bestSource = doc.description || cleanBody || doc.headings || '';
        var bestWinStart = 0;
        var bestScore = -1;
        var winLen = 140;

        var terms = parsed ? parsed.highlightTerms : [];
        for (var ci = 0; ci < candidates.length; ci++) {
            var src = candidates[ci].text;
            if (!src) continue;
            var normSrc = normalizeText(src);

            // Collect hit positions in normSrc
            var hits = [];
            for (var ti = 0; ti < terms.length; ti++) {
                var t = terms[ti];
                if (!t || (t.length === 1 && CJK_STOP_CHARS[t] && parsed.norm.length > 1)) continue;
                var isShortAscii = /^[a-z0-9]+$/.test(t) && t.length <= 2;
                var pos = normSrc.indexOf(t);
                var count = 0;
                while (pos !== -1 && count < 6) {
                    var ok = true;
                    if (isShortAscii) {
                        var bc = pos > 0 ? normSrc.charAt(pos - 1) : '';
                        var ac = pos + t.length < normSrc.length ? normSrc.charAt(pos + t.length) : '';
                        if (isAsciiAlnum(bc) || isAsciiAlnum(ac)) ok = false;
                    }
                    if (ok) {
                        hits.push({ pos: pos, weight: t.length * t.length });
                        count++;
                    }
                    pos = normSrc.indexOf(t, pos + 1);
                }
            }

            if (hits.length === 0) continue;

            for (var hi = 0; hi < hits.length; hi++) {
                var center = hits[hi].pos;
                var wStart = Math.max(0, center - 38);
                var wEnd = wStart + winLen;
                var wScore = 0;
                for (var hj = 0; hj < hits.length; hj++) {
                    if (hits[hj].pos >= wStart && hits[hj].pos < wEnd) {
                        wScore += hits[hj].weight;
                    }
                }
                wScore *= candidates[ci].bonus;
                if (wScore > bestScore) {
                    bestScore = wScore;
                    bestSource = src;
                    bestWinStart = Math.min(wStart, Math.max(0, src.length - winLen));
                }
            }
        }

        if (!bestSource) return '';
        var start = bestWinStart;
        // Snap start slightly to natural punctuation boundary if nearby
        if (start > 0) {
            var boundarySlice = bestSource.slice(Math.max(0, start - 12), start + 8);
            var puncMatch = boundarySlice.match(/[。！？；.!?;，,\s]/);
            if (puncMatch && puncMatch.index !== undefined) {
                var snapped = Math.max(0, start - 12) + puncMatch.index + 1;
                if (snapped < bestSource.length - 30) start = snapped;
            }
        }

        var end = Math.min(bestSource.length, start + winLen);
        var slice = bestSource.slice(start, end).trim();
        var prefix = start > 0 ? '…' : '';
        var suffix = end < bestSource.length ? '…' : '';
        return prefix + buildHighlightedHtml(slice, parsed) + suffix;
    }

    // =========================================================================
    // Browser UI Controller (only runs when `document` exists)
    // =========================================================================
    function getUiStrings() {
        var lang = (typeof document !== 'undefined' && document.documentElement.lang || 'zh-CN').toLowerCase();
        if (lang.indexOf('zh-tw') === 0 || lang.indexOf('zh-hk') === 0 || lang.indexOf('zh-hant') === 0) {
            return {
                placeholder: '搜尋文章、技術關鍵詞、標籤…',
                loading: '正在載入搜尋索引…',
                hydrating: '全文索引同步中…',
                resultsCount: function (n) { return '找到 ' + n + ' 篇相關內容'; },
                noResultsTitle: function (q) { return '未找到與「' + escapeHtml(q) + '」相關的結果'; },
                noResultsHint: '試試更簡短的關鍵詞、英文術語，或點擊下方熱門主題：',
                popularTopics: '熱門搜尋',
                recentPosts: '最新文章',
                typePost: '文章',
                typeProject: '方案',
                typeReport: '報告',
                typePage: '頁面',
                navHint: '↑↓ 選擇 · Enter 開啟 · Esc 關閉',
                close: '關閉'
            };
        }
        if (lang.indexOf('zh') !== 0) {
            return {
                placeholder: 'Search articles, keywords, tags…',
                loading: 'Loading search index…',
                hydrating: 'Syncing full-text…',
                resultsCount: function (n) { return n + (n === 1 ? ' result found' : ' results found'); },
                noResultsTitle: function (q) { return 'No results found for "' + escapeHtml(q) + '"'; },
                noResultsHint: 'Try shorter keywords, technical terms, or explore popular topics:',
                popularTopics: 'Popular Topics',
                recentPosts: 'Latest Articles',
                typePost: 'Post',
                typeProject: 'Solution',
                typeReport: 'Report',
                typePage: 'Page',
                navHint: '↑↓ Navigate · Enter Open · Esc Close',
                close: 'Close'
            };
        }
        return {
            placeholder: '搜索文章标题、正文关键词、标签…',
            loading: '正在加载搜索索引…',
            hydrating: '全文深度索引同步中…',
            resultsCount: function (n) { return '找到 ' + n + ' 条相关内容'; },
            noResultsTitle: function (q) { return '未找到“' + escapeHtml(q) + '”的相关结果'; },
            noResultsHint: '建议缩短关键词、换个核心词，或直接点击下方热门主题：',
            popularTopics: '热门搜索',
            recentPosts: '最新文章',
            typePost: '文章',
            typeProject: '方案',
            typeReport: '报告',
            typePage: '页面',
            navHint: '↑↓ 选择 · Enter 打开 · Esc 关闭',
            close: '关闭'
        };
    }

    var POPULAR_CHIPS = ['AI Agent', 'Claude', '大模型', '私有化部署', '离开大厂', '英伟达', 'OpenClaw', 'DevOps', '算力'];

    function initBrowserSearch(config) {
        if (typeof document === 'undefined') return;
        var baseUrl = (config && config.baseUrl) || '';
        var docsEndpoint = baseUrl + '/assets/data/search-documents.json';
        var fulltextEndpoint = baseUrl + '/assets/data/search-fulltext.json';

        var engine = new SearchEngine();
        var tier1Loaded = false;
        var tier1Loading = false;
        var tier2Started = false;
        var activeIndex = -1;
        var currentQuery = '';
        var isComposing = false;
        var debounceTimer = null;
        var gaTimer = null;

        var resultsRoot = document.getElementById('lunrsearchresults');
        var navInput = document.getElementById('lunrsearch');

        function ensureDataLoaded(callback) {
            if (tier1Loaded) {
                if (callback) callback();
                return;
            }
            if (tier1Loading) {
                if (callback) {
                    var checkIv = setInterval(function () {
                        if (tier1Loaded) {
                            clearInterval(checkIv);
                            callback();
                        }
                    }, 30);
                }
                return;
            }
            tier1Loading = true;

            fetch(docsEndpoint, { credentials: 'same-origin' })
                .then(function (r) {
                    if (!r.ok) throw new Error('HTTP ' + r.status);
                    return r.json();
                })
                .then(function (data) {
                    engine.loadDocuments(Array.isArray(data) ? data : []);
                })
                .catch(function (err) {
                    console.error('[Search] Failed to load search-documents.json:', err);
                    engine.loadDocuments([]);
                })
                .finally(function () {
                    tier1Loaded = true;
                    tier1Loading = false;
                    if (callback) callback();
                    startFulltextHydration();
                });
        }

        function startFulltextHydration() {
            if (tier2Started) return;
            tier2Started = true;
            var runFetch = function () {
                fetch(fulltextEndpoint, { credentials: 'same-origin' })
                    .then(function (r) {
                        if (!r.ok) throw new Error('HTTP ' + r.status);
                        return r.json();
                    })
                    .then(function (ftMap) {
                        engine.hydrateFulltext(ftMap, function () {
                            // Refresh active search results seamlessly once full body is indexed!
                            if (isModalOpen() && currentQuery.trim()) {
                                renderResults(currentQuery, true);
                            }
                            updateStatusBadge();
                        }, true);
                    })
                    .catch(function () {
                        engine.fulltextHydrated = true;
                        updateStatusBadge();
                    });
            };
            if (typeof requestIdleCallback === 'function') {
                requestIdleCallback(runFetch, { timeout: 600 });
            } else {
                setTimeout(runFetch, 120);
            }
        }

        function isModalOpen() {
            return !!(resultsRoot && resultsRoot.style.display === 'block');
        }

        function ensureModalDom() {
            if (!resultsRoot) {
                resultsRoot = document.createElement('div');
                resultsRoot.id = 'lunrsearchresults';
                document.body.appendChild(resultsRoot);
            }
            if (document.getElementById('resultsmodal')) {
                var i18nNow = getUiStrings();
                var inp = document.getElementById('modalSearchInput');
                if (inp) inp.placeholder = i18nNow.placeholder;
                return;
            }

            var ui = getUiStrings();
            resultsRoot.innerHTML =
                '<div id="resultsmodal" class="jj-search-backdrop" role="dialog" aria-modal="true" aria-label="Site search">' +
                    '<div class="jj-search-dialog" role="document">' +
                        '<div class="jj-search-header">' +
                            '<svg class="jj-search-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" viewBox="0 0 16 16" aria-hidden="true">' +
                                '<path d="M11.742 10.344a6.5 6.5 0 1 0-1.398 1.398h.001l3.85 3.85a1 1 0 0 0 1.414-1.415l-3.85-3.85zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>' +
                            '</svg>' +
                            '<input type="search" id="modalSearchInput" class="jj-search-input" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="' + escapeHtml(ui.placeholder) + '" aria-label="Search">' +
                            '<button type="button" id="modalSearchClear" class="jj-search-clear" aria-label="Clear search" style="display:none">&times;</button>' +
                            '<button type="button" id="btnx" class="jj-search-esc" aria-label="' + escapeHtml(ui.close) + '">ESC</button>' +
                        '</div>' +
                        '<div id="jjSearchMeta" class="jj-search-meta" style="display:none"></div>' +
                        '<div id="jjSearchBody" class="jj-search-body">' +
                            '<ul id="jjSearchList" class="jj-search-list" role="listbox" aria-live="polite"></ul>' +
                        '</div>' +
                        '<div class="jj-search-footer">' +
                            '<span class="jj-search-hint">' + escapeHtml(ui.navHint) + '</span>' +
                            '<span id="jjHydrateStatus" class="jj-hydrate-status"></span>' +
                        '</div>' +
                    '</div>' +
                '</div>';

            var modalBackdrop = document.getElementById('resultsmodal');
            var modalInput = document.getElementById('modalSearchInput');
            var clearBtn = document.getElementById('modalSearchClear');
            var closeBtn = document.getElementById('btnx');
            var listEl = document.getElementById('jjSearchList');

            modalBackdrop.addEventListener('mousedown', function (e) {
                if (e.target === modalBackdrop) {
                    closeModal();
                }
            });

            closeBtn.addEventListener('click', function () {
                closeModal();
            });

            clearBtn.addEventListener('click', function () {
                modalInput.value = '';
                clearBtn.style.display = 'none';
                currentQuery = '';
                if (navInput) navInput.value = '';
                renderEmptyState();
                modalInput.focus();
            });

            modalInput.addEventListener('compositionstart', function () {
                isComposing = true;
            });

            modalInput.addEventListener('compositionend', function () {
                isComposing = false;
                triggerInputSearch(modalInput.value);
            });

            modalInput.addEventListener('input', function () {
                var val = modalInput.value;
                clearBtn.style.display = val ? 'inline-flex' : 'none';
                if (isComposing) return;
                triggerInputSearch(val);
            });

            modalInput.addEventListener('keydown', function (e) {
                if (isComposing) return;
                var items = listEl.querySelectorAll('a.jj-result-link');
                if (e.key === 'ArrowDown') {
                    if (items.length > 0) {
                        e.preventDefault();
                        setActiveItem((activeIndex + 1) % items.length, items);
                    }
                } else if (e.key === 'ArrowUp') {
                    if (items.length > 0) {
                        e.preventDefault();
                        setActiveItem((activeIndex - 1 + items.length) % items.length, items);
                    }
                } else if (e.key === 'Enter') {
                    e.preventDefault();
                    if (items.length > 0) {
                        var targetIdx = activeIndex >= 0 && activeIndex < items.length ? activeIndex : 0;
                        items[targetIdx].click();
                    } else if (modalInput.value.trim()) {
                        renderResults(modalInput.value, false);
                    }
                } else if (e.key === 'Escape') {
                    e.preventDefault();
                    closeModal();
                }
            });

            listEl.addEventListener('click', function (e) {
                var chip = e.target.closest('[data-search-chip]');
                if (chip) {
                    e.preventDefault();
                    var q = chip.getAttribute('data-search-chip') || '';
                    modalInput.value = q;
                    clearBtn.style.display = q ? 'inline-flex' : 'none';
                    modalInput.focus();
                    triggerInputSearch(q, true);
                }
            });
        }

        function setActiveItem(newIdx, items) {
            for (var i = 0; i < items.length; i++) {
                if (i === newIdx) {
                    items[i].classList.add('active');
                    items[i].scrollIntoView({ block: 'nearest' });
                } else {
                    items[i].classList.remove('active');
                }
            }
            activeIndex = newIdx;
        }

        function updateStatusBadge() {
            var el = document.getElementById('jjHydrateStatus');
            if (!el) return;
            var ui = getUiStrings();
            if (tier1Loaded && !engine.fulltextHydrated) {
                el.textContent = ui.hydrating;
            } else {
                el.textContent = '';
            }
        }

        function triggerInputSearch(val, immediate) {
            clearTimeout(debounceTimer);
            currentQuery = val;
            if (navInput) navInput.value = val;

            if (!val || !val.trim()) {
                renderEmptyState();
                return;
            }

            var run = function () {
                ensureDataLoaded(function () {
                    renderResults(val, false);
                });
            };

            if (immediate) {
                run();
            } else {
                debounceTimer = setTimeout(run, 60);
            }

            // GA4 analytics tracking
            clearTimeout(gaTimer);
            gaTimer = setTimeout(function () {
                if (val.trim().length >= 2 && typeof window.gtag === 'function') {
                    window.gtag('event', 'site_search', {
                        search_term: val.trim(),
                        page_location: window.location.href
                    });
                }
            }, 900);
        }

        function getTypeBadge(doc, ui) {
            if (doc.type === 'project') return { label: ui.typeProject, cls: 'jj-badge-project' };
            if (doc.type === 'report') return { label: ui.typeReport, cls: 'jj-badge-report' };
            if (doc.type === 'page') return { label: ui.typePage, cls: 'jj-badge-page' };
            var cat = doc.categories && doc.categories.length > 0 ? doc.categories[0] : ui.typePost;
            return { label: cat, cls: 'jj-badge-post' };
        }

        function renderEmptyState() {
            var metaEl = document.getElementById('jjSearchMeta');
            var listEl = document.getElementById('jjSearchList');
            if (!listEl) return;
            var ui = getUiStrings();
            activeIndex = -1;
            if (metaEl) metaEl.style.display = 'none';
            updateStatusBadge();

            var chipsHtml = POPULAR_CHIPS.map(function (c) {
                return '<button type="button" class="jj-chip" data-search-chip="' + escapeHtml(c) + '">' + escapeHtml(c) + '</button>';
            }).join('');

            var html = '<li class="jj-empty-section">' +
                '<div class="jj-section-label">' + escapeHtml(ui.popularTopics) + '</div>' +
                '<div class="jj-chips-wrap">' + chipsHtml + '</div>' +
                '</li>';

            if (tier1Loaded && engine.docs.length > 0) {
                var posts = engine.docs.filter(function (d) { return d.type === 'post'; }).slice(0, 5);
                if (posts.length > 0) {
                    html += '<li class="jj-section-divider">' + escapeHtml(ui.recentPosts) + '</li>';
                    for (var i = 0; i < posts.length; i++) {
                        var p = posts[i];
                        var badge = getTypeBadge(p, ui);
                        html += '<li class="jj-result-item" role="option">' +
                            '<a href="' + escapeHtml(p.url) + '" class="jj-result-link">' +
                                '<div class="jj-result-top">' +
                                    '<span class="jj-badge ' + badge.cls + '">' + escapeHtml(badge.label) + '</span>' +
                                    (p.date ? '<span class="jj-result-date">' + escapeHtml(p.date) + '</span>' : '') +
                                '</div>' +
                                '<div class="jj-result-title">' + escapeHtml(p.title) + '</div>' +
                            '</a>' +
                        '</li>';
                    }
                }
            } else if (!tier1Loaded) {
                html += '<li class="jj-loading-row">' + escapeHtml(ui.loading) + '</li>';
            }

            listEl.innerHTML = html;
        }

        function renderResults(query, preserveSelection) {
            var metaEl = document.getElementById('jjSearchMeta');
            var listEl = document.getElementById('jjSearchList');
            if (!listEl) return;
            var ui = getUiStrings();
            updateStatusBadge();

            var q = (query || '').trim();
            if (!q) {
                renderEmptyState();
                return;
            }

            if (!tier1Loaded) {
                if (metaEl) metaEl.style.display = 'none';
                listEl.innerHTML = '<li class="jj-loading-row">' + escapeHtml(ui.loading) + '</li>';
                return;
            }

            var results = engine.search(q, { limit: 30 });
            if (!preserveSelection) activeIndex = results.length > 0 ? 0 : -1;

            if (results.length > 0) {
                if (metaEl) {
                    metaEl.textContent = ui.resultsCount(results.length);
                    metaEl.style.display = 'block';
                }

                var parsedForTags = parseQuery(q);
                var itemsHtml = '';
                for (var i = 0; i < results.length; i++) {
                    var r = results[i];
                    var d = r.doc;
                    var badge = getTypeBadge(d, ui);
                    var isAct = i === activeIndex;

                    // Show up to 3 tags (prioritizing matched tags)
                    var displayTags = [];
                    if (d.tags && d.tags.length > 0) {
                        var qNorm = parsedForTags ? parsedForTags.norm : '';
                        var matchedT = [];
                        var otherT = [];
                        for (var ti = 0; ti < d.tags.length; ti++) {
                            var tg = d.tags[ti];
                            var tgNorm = normalizeText(tg);
                            if (qNorm && (tgNorm.indexOf(qNorm) !== -1 || qNorm.indexOf(tgNorm) !== -1)) {
                                matchedT.push(tg);
                            } else {
                                otherT.push(tg);
                            }
                        }
                        displayTags = matchedT.concat(otherT).slice(0, 3);
                    }

                    var tagsHtml = '';
                    for (var dt = 0; dt < displayTags.length; dt++) {
                        tagsHtml += '<span class="jj-result-tag">#' + buildHighlightedHtml(displayTags[dt], parsedForTags) + '</span>';
                    }

                    var externalAttr = /^https?:\/\//i.test(d.url) && d.url.indexOf(window.location.host) === -1
                        ? ' target="_blank" rel="noopener"'
                        : '';

                    itemsHtml += '<li class="jj-result-item" role="option">' +
                        '<a href="' + escapeHtml(d.url) + '" class="jj-result-link' + (isAct ? ' active' : '') + '"' + externalAttr + '>' +
                            '<div class="jj-result-top">' +
                                '<span class="jj-badge ' + badge.cls + '">' + escapeHtml(badge.label) + '</span>' +
                                (d.date ? '<span class="jj-result-date">' + escapeHtml(d.date) + '</span>' : '') +
                                tagsHtml +
                            '</div>' +
                            '<div class="jj-result-title">' + r.titleHtml + '</div>' +
                            (r.snippetHtml ? '<div class="jj-result-snippet">' + r.snippetHtml + '</div>' : '') +
                        '</a>' +
                    '</li>';
                }
                listEl.innerHTML = itemsHtml;
            } else {
                if (metaEl) metaEl.style.display = 'none';
                var chipsHtml = POPULAR_CHIPS.map(function (c) {
                    return '<button type="button" class="jj-chip" data-search-chip="' + escapeHtml(c) + '">' + escapeHtml(c) + '</button>';
                }).join('');

                listEl.innerHTML = '<li class="jj-no-results">' +
                    '<div class="jj-no-results-title">' + ui.noResultsTitle(q) + '</div>' +
                    '<div class="jj-no-results-hint">' + escapeHtml(ui.noResultsHint) + '</div>' +
                    '<div class="jj-chips-wrap justify-center">' + chipsHtml + '</div>' +
                '</li>';
            }
        }

        function openModal(initialTerm) {
            ensureModalDom();
            resultsRoot.style.display = 'block';
            document.body.classList.add('modal-open');

            var modalInput = document.getElementById('modalSearchInput');
            var clearBtn = document.getElementById('modalSearchClear');
            var term = typeof initialTerm === 'string' ? initialTerm : (navInput && navInput.value ? navInput.value : currentQuery);

            if (modalInput) {
                modalInput.value = term || '';
                if (clearBtn) clearBtn.style.display = modalInput.value ? 'inline-flex' : 'none';
            }

            currentQuery = term || '';
            if (currentQuery.trim()) {
                renderResults(currentQuery, false);
                ensureDataLoaded(function () {
                    renderResults(currentQuery, false);
                });
            } else {
                renderEmptyState();
                ensureDataLoaded(function () {
                    if (!currentQuery.trim() && isModalOpen()) {
                        renderEmptyState();
                    }
                });
            }

            setTimeout(function () {
                if (modalInput) {
                    modalInput.focus();
                    if (modalInput.value) {
                        modalInput.setSelectionRange(modalInput.value.length, modalInput.value.length);
                    }
                }
            }, 20);
        }

        function closeModal() {
            if (!resultsRoot) return;
            resultsRoot.style.display = 'none';
            document.body.classList.remove('modal-open');
        }

        // Global Esc listener when modal is open
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && isModalOpen()) {
                e.preventDefault();
                closeModal();
            }
        });

        // Expose public API for navbar hooks & backward compatibility
        window.openSearchModal = openModal;
        window.closeSearchModal = closeModal;
        window.lunr_search = function (term) {
            openModal(term || '');
            return false;
        };
    }

    return {
        SearchEngine: SearchEngine,
        normalizeText: normalizeText,
        parseQuery: parseQuery,
        tokenizeForIndex: tokenizeForIndex,
        buildHighlightedHtml: buildHighlightedHtml,
        initBrowserSearch: initBrowserSearch
    };
});
