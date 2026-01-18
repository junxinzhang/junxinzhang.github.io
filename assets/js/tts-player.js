/**
 * TTS Player - Text-to-Speech for Blog Articles
 * Uses Web Speech API for browser-native speech synthesis
 */
(function() {
    'use strict';

    // Check if Speech Synthesis is supported
    if (!('speechSynthesis' in window)) {
        console.warn('TTS: Speech Synthesis not supported in this browser');
        return;
    }

    var synth = window.speechSynthesis;
    var utterance = null;
    var isPlaying = false;
    var isPaused = false;
    var currentRate = 1.0;
    var articleText = '';
    var currentCharIndex = 0;
    var totalChars = 0;
    var progressInterval = null;
    var voices = [];
    var playStartTime = null;  // Track play start time for duration calculation

    // Analytics helper function
    function trackTTSEvent(action, params) {
        params = params || {};

        // Get article info for context
        var articleTitle = document.title || '';
        var articlePath = window.location.pathname || '';

        // Merge default params
        var eventParams = {
            event_category: 'TTS_Player',
            article_title: articleTitle,
            article_path: articlePath,
            article_length: totalChars,
            language: document.documentElement.lang || 'zh-hans'
        };

        // Add custom params
        for (var key in params) {
            if (params.hasOwnProperty(key)) {
                eventParams[key] = params[key];
            }
        }

        // Send to Google Analytics 4
        if (typeof gtag === 'function') {
            gtag('event', action, eventParams);
        }

        // Also log to console in development
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            console.log('TTS Analytics:', action, eventParams);
        }
    }

    // DOM Elements
    var player = null;
    var playBtn = null;
    var stopBtn = null;
    var speedBtn = null;
    var progressBar = null;
    var timeDisplay = null;
    var statusText = null;

    // Speed options
    var speeds = [0.75, 1.0, 1.25, 1.5, 2.0];
    var speedLabels = ['0.75x', '1x', '1.25x', '1.5x', '2x'];
    var currentSpeedIndex = 1;

    // Initialize when DOM is ready
    document.addEventListener('DOMContentLoaded', init);

    function init() {
        // Only initialize on article pages
        var article = document.querySelector('article.article-post');
        if (!article) return;

        // Get article text
        articleText = extractArticleText(article);
        if (!articleText || articleText.length < 50) return;

        totalChars = articleText.length;

        // Load voices
        loadVoices();

        // Create player UI
        createPlayerUI();

        // Bind events
        bindEvents();
    }

    function loadVoices() {
        voices = synth.getVoices();

        // Chrome loads voices asynchronously
        if (voices.length === 0) {
            synth.onvoiceschanged = function() {
                voices = synth.getVoices();
            };
        }
    }

    function getBestVoice() {
        // Get page language
        var lang = document.documentElement.lang || 'zh-CN';

        // Map common language codes
        var langMap = {
            'zh-hans': 'zh-CN',
            'zh-hant': 'zh-TW',
            'en': 'en-US',
            'ja': 'ja-JP',
            'ko': 'ko-KR',
            'de': 'de-DE',
            'fr': 'fr-FR',
            'es': 'es-ES',
            'it': 'it-IT',
            'pt': 'pt-BR',
            'hi': 'hi-IN'
        };

        var targetLang = langMap[lang] || lang;

        // Find best matching voice
        var voice = null;

        // Priority: local voice > remote voice
        for (var i = 0; i < voices.length; i++) {
            if (voices[i].lang.startsWith(targetLang.split('-')[0])) {
                if (!voice || voices[i].localService) {
                    voice = voices[i];
                    if (voices[i].localService) break;
                }
            }
        }

        return voice;
    }

    function extractArticleText(article) {
        // Clone the article to avoid modifying the original
        var clone = article.cloneNode(true);

        // Remove elements that shouldn't be read
        var removeSelectors = [
            'script', 'style', 'code', 'pre', 'figure', 'img',
            '.highlight', '.language-', '[class*="code"]',
            'table', 'iframe', 'video', 'audio', '.tts-player'
        ];

        removeSelectors.forEach(function(selector) {
            var elements = clone.querySelectorAll(selector);
            elements.forEach(function(el) {
                el.remove();
            });
        });

        // Get text and clean it up
        var text = clone.textContent || clone.innerText || '';

        // Clean up whitespace and special characters
        text = text
            .replace(/\s+/g, ' ')           // Normalize whitespace
            .replace(/[#*`_~\[\]]/g, '')    // Remove markdown chars
            .replace(/https?:\/\/\S+/g, '') // Remove URLs
            .replace(/\{[^}]*\}/g, '')      // Remove template syntax
            .trim();

        return text;
    }

    function createPlayerUI() {
        // Create player container
        player = document.createElement('div');
        player.className = 'tts-player';
        player.innerHTML =
            '<div class="tts-player-inner">' +
                '<div class="tts-icon">' +
                    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">' +
                        '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>' +
                        '<path d="M19 10v2a7 7 0 0 1-14 0v-2"/>' +
                        '<line x1="12" y1="19" x2="12" y2="23"/>' +
                        '<line x1="8" y1="23" x2="16" y2="23"/>' +
                    '</svg>' +
                '</div>' +
                '<div class="tts-content">' +
                    '<div class="tts-header">' +
                        '<span class="tts-title" data-i18n="tts.listen_article"></span>' +
                        '<span class="tts-status"></span>' +
                    '</div>' +
                    '<div class="tts-progress-container">' +
                        '<div class="tts-progress-bar">' +
                            '<div class="tts-progress-fill"></div>' +
                        '</div>' +
                        '<span class="tts-time">0:00</span>' +
                    '</div>' +
                '</div>' +
                '<div class="tts-controls">' +
                    '<button class="tts-btn tts-play-btn" aria-label="Play" title="Play">' +
                        '<svg class="tts-icon-play" viewBox="0 0 24 24" fill="currentColor">' +
                            '<path d="M8 5v14l11-7z"/>' +
                        '</svg>' +
                        '<svg class="tts-icon-pause" viewBox="0 0 24 24" fill="currentColor" style="display:none">' +
                            '<path d="M6 4h4v16H6V4zm8 0h4v16h-4V4z"/>' +
                        '</svg>' +
                    '</button>' +
                    '<button class="tts-btn tts-stop-btn" aria-label="Stop" title="Stop">' +
                        '<svg viewBox="0 0 24 24" fill="currentColor">' +
                            '<rect x="6" y="6" width="12" height="12"/>' +
                        '</svg>' +
                    '</button>' +
                    '<button class="tts-btn tts-speed-btn" aria-label="Speed" title="Speed">' +
                        '<span>1x</span>' +
                    '</button>' +
                '</div>' +
            '</div>';

        // Get references to elements
        playBtn = player.querySelector('.tts-play-btn');
        stopBtn = player.querySelector('.tts-stop-btn');
        speedBtn = player.querySelector('.tts-speed-btn');
        progressBar = player.querySelector('.tts-progress-fill');
        timeDisplay = player.querySelector('.tts-time');
        statusText = player.querySelector('.tts-status');

        // Set initial title text
        var titleEl = player.querySelector('.tts-title');
        titleEl.textContent = getTTSText('listen_article');

        // Insert after article headline
        var headline = document.querySelector('.article-headline');
        var metaSpan = document.querySelector('.jumbotron .text-muted');

        if (metaSpan && metaSpan.parentNode) {
            metaSpan.parentNode.insertBefore(player, metaSpan.nextSibling);
        } else if (headline && headline.parentNode) {
            headline.parentNode.insertBefore(player, headline.nextSibling);
        }

        // Update estimated time
        updateEstimatedTime();
    }

    function getTTSText(key) {
        var lang = document.documentElement.lang || 'zh-hans';
        var texts = {
            'zh-hans': {
                'listen_article': '听文章',
                'playing': '播放中',
                'paused': '已暂停',
                'ready': '点击播放'
            },
            'zh-hant': {
                'listen_article': '聽文章',
                'playing': '播放中',
                'paused': '已暫停',
                'ready': '點擊播放'
            },
            'en': {
                'listen_article': 'Listen to Article',
                'playing': 'Playing',
                'paused': 'Paused',
                'ready': 'Click to play'
            },
            'ja': {
                'listen_article': '記事を聞く',
                'playing': '再生中',
                'paused': '一時停止',
                'ready': 'クリックして再生'
            },
            'ko': {
                'listen_article': '기사 듣기',
                'playing': '재생 중',
                'paused': '일시 정지',
                'ready': '클릭하여 재생'
            }
        };

        var langTexts = texts[lang] || texts['en'];
        return langTexts[key] || texts['en'][key] || key;
    }

    function bindEvents() {
        playBtn.addEventListener('click', togglePlay);
        stopBtn.addEventListener('click', stop);
        speedBtn.addEventListener('click', cycleSpeed);

        // Handle page visibility change
        document.addEventListener('visibilitychange', function() {
            if (document.hidden && isPlaying && !isPaused) {
                // Continue playing in background (most browsers support this)
            }
        });

        // Clean up on page unload
        window.addEventListener('beforeunload', function() {
            synth.cancel();
        });
    }

    function togglePlay() {
        if (isPlaying && !isPaused) {
            pause();
        } else if (isPaused) {
            resume();
        } else {
            play();
        }
    }

    function play() {
        if (!articleText) return;

        synth.cancel();

        utterance = new SpeechSynthesisUtterance(articleText);
        utterance.rate = currentRate;
        utterance.pitch = 1;
        utterance.volume = 1;

        var voice = getBestVoice();
        if (voice) {
            utterance.voice = voice;
            utterance.lang = voice.lang;
        }

        utterance.onstart = function() {
            isPlaying = true;
            isPaused = false;
            playStartTime = Date.now();
            updateUI();
            startProgressTracking();

            // Track play start event
            trackTTSEvent('tts_play', {
                speed: currentRate,
                voice_name: voice ? voice.name : 'default',
                estimated_duration: Math.floor(totalChars / (5 * currentRate))
            });
        };

        utterance.onend = function() {
            isPlaying = false;
            isPaused = false;

            // Calculate actual listening duration
            var listenDuration = playStartTime ? Math.floor((Date.now() - playStartTime) / 1000) : 0;
            var completionRate = Math.round((currentCharIndex / totalChars) * 100);

            // Track completion event
            trackTTSEvent('tts_complete', {
                listen_duration: listenDuration,
                completion_rate: completionRate,
                speed: currentRate
            });

            currentCharIndex = 0;
            playStartTime = null;
            updateUI();
            stopProgressTracking();
            resetProgress();
        };

        utterance.onerror = function(event) {
            console.error('TTS Error:', event.error);
            isPlaying = false;
            isPaused = false;
            updateUI();
            stopProgressTracking();
        };

        utterance.onpause = function() {
            isPaused = true;
            updateUI();
        };

        utterance.onresume = function() {
            isPaused = false;
            updateUI();
        };

        utterance.onboundary = function(event) {
            if (event.name === 'word' || event.name === 'sentence') {
                currentCharIndex = event.charIndex;
            }
        };

        synth.speak(utterance);
    }

    function pause() {
        if (synth.speaking) {
            synth.pause();
            isPaused = true;
            updateUI();

            // Track pause event
            var progressPercent = Math.round((currentCharIndex / totalChars) * 100);
            trackTTSEvent('tts_pause', {
                progress_percent: progressPercent,
                speed: currentRate
            });
        }
    }

    function resume() {
        if (synth.paused) {
            synth.resume();
            isPaused = false;
            updateUI();

            // Track resume event
            var progressPercent = Math.round((currentCharIndex / totalChars) * 100);
            trackTTSEvent('tts_resume', {
                progress_percent: progressPercent,
                speed: currentRate
            });
        }
    }

    function stop() {
        // Calculate listening stats before resetting
        var listenDuration = playStartTime ? Math.floor((Date.now() - playStartTime) / 1000) : 0;
        var progressPercent = Math.round((currentCharIndex / totalChars) * 100);

        // Track stop event (only if was actually playing)
        if (isPlaying || isPaused) {
            trackTTSEvent('tts_stop', {
                listen_duration: listenDuration,
                progress_percent: progressPercent,
                speed: currentRate
            });
        }

        synth.cancel();
        isPlaying = false;
        isPaused = false;
        currentCharIndex = 0;
        playStartTime = null;
        updateUI();
        stopProgressTracking();
        resetProgress();
    }

    function cycleSpeed() {
        var oldRate = currentRate;
        currentSpeedIndex = (currentSpeedIndex + 1) % speeds.length;
        currentRate = speeds[currentSpeedIndex];
        speedBtn.querySelector('span').textContent = speedLabels[currentSpeedIndex];

        // Track speed change event
        trackTTSEvent('tts_speed_change', {
            old_speed: oldRate,
            new_speed: currentRate,
            is_playing: isPlaying
        });

        // If currently playing, restart with new speed
        if (isPlaying) {
            var progress = currentCharIndex / totalChars;
            stop();
            // Restart from approximate position
            var startIndex = Math.floor(progress * articleText.length);
            var remainingText = articleText.substring(startIndex);

            utterance = new SpeechSynthesisUtterance(remainingText);
            utterance.rate = currentRate;

            var voice = getBestVoice();
            if (voice) {
                utterance.voice = voice;
                utterance.lang = voice.lang;
            }

            utterance.onstart = function() {
                isPlaying = true;
                isPaused = false;
                updateUI();
                startProgressTracking();
            };

            utterance.onend = function() {
                isPlaying = false;
                isPaused = false;
                currentCharIndex = 0;
                updateUI();
                stopProgressTracking();
                resetProgress();
            };

            synth.speak(utterance);
        }

        updateEstimatedTime();
    }

    function updateUI() {
        var playIcon = playBtn.querySelector('.tts-icon-play');
        var pauseIcon = playBtn.querySelector('.tts-icon-pause');

        if (isPlaying && !isPaused) {
            playIcon.style.display = 'none';
            pauseIcon.style.display = 'block';
            player.classList.add('tts-playing');
            player.classList.remove('tts-paused');
            statusText.textContent = getTTSText('playing');
        } else if (isPaused) {
            playIcon.style.display = 'block';
            pauseIcon.style.display = 'none';
            player.classList.remove('tts-playing');
            player.classList.add('tts-paused');
            statusText.textContent = getTTSText('paused');
        } else {
            playIcon.style.display = 'block';
            pauseIcon.style.display = 'none';
            player.classList.remove('tts-playing', 'tts-paused');
            statusText.textContent = '';
        }
    }

    function startProgressTracking() {
        stopProgressTracking();
        progressInterval = setInterval(updateProgress, 100);
    }

    function stopProgressTracking() {
        if (progressInterval) {
            clearInterval(progressInterval);
            progressInterval = null;
        }
    }

    function updateProgress() {
        if (!isPlaying || isPaused) return;

        // Estimate progress based on speech rate and elapsed time
        var charsPerSecond = 5 * currentRate; // Approximate Chinese reading speed
        currentCharIndex += charsPerSecond * 0.1; // 100ms interval

        if (currentCharIndex > totalChars) {
            currentCharIndex = totalChars;
        }

        var progress = (currentCharIndex / totalChars) * 100;
        progressBar.style.width = progress + '%';

        // Update time display
        var elapsedSeconds = Math.floor(currentCharIndex / (5 * currentRate));
        var totalSeconds = Math.floor(totalChars / (5 * currentRate));
        var remainingSeconds = totalSeconds - elapsedSeconds;

        timeDisplay.textContent = formatTime(elapsedSeconds) + ' / ' + formatTime(totalSeconds);
    }

    function resetProgress() {
        progressBar.style.width = '0%';
        updateEstimatedTime();
    }

    function updateEstimatedTime() {
        var totalSeconds = Math.floor(totalChars / (5 * currentRate));
        timeDisplay.textContent = formatTime(totalSeconds);
    }

    function formatTime(seconds) {
        var mins = Math.floor(seconds / 60);
        var secs = Math.floor(seconds % 60);
        return mins + ':' + (secs < 10 ? '0' : '') + secs;
    }

})();
