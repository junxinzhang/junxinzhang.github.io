(() => {
  const form = document.getElementById('storyForm');
  const titleEl = document.getElementById('bookTitle');
  const pageEl = document.getElementById('bookPage');
  const pageArt = document.getElementById('pageArt');
  const pageNumber = document.getElementById('pageNumber');
  const pageHeading = document.getElementById('pageHeading');
  const pageText = document.getElementById('pageText');
  const thumbs = document.getElementById('thumbnailRow');
  const reader = document.getElementById('reader');
  const readerPage = document.getElementById('readerPage');
  const readerTitle = document.getElementById('readerTitle');
  const saveStatus = document.getElementById('saveStatus');

  const defaults = {
    childName: '小雨',
    childAge: '5',
    childRole: '她',
    theme: '勇气',
    style: '水彩绘本',
    traits: '喜欢恐龙、怕黑，但很会照顾朋友',
    details: '家里的小黄鸭玩具、睡前要抱的蓝色毯子'
  };

  const samples = {
    bedtime: {
      childName: '安安',
      childAge: '4',
      childRole: '他',
      theme: '睡觉',
      style: '水彩绘本',
      traits: '怕黑，喜欢小船和月亮',
      details: '床头的小海豚灯、每天睡前听的一首歌'
    },
    friendship: {
      childName: '朵朵',
      childAge: '6',
      childRole: '她',
      theme: '分享',
      style: '剪纸拼贴',
      traits: '喜欢烤饼干，有一点护食，但很想交朋友',
      details: '周末去公园、背包里的星星贴纸'
    },
    confidence: {
      childName: '乐乐',
      childAge: '7',
      childRole: '他',
      theme: '自信',
      style: '蜡笔童画',
      traits: '说话声音小，画画很认真',
      details: '幼儿园的蓝色小舞台、一支红色蜡笔'
    }
  };

  const themeData = {
    '勇气': {
      title: name => `${name}和会发光的口袋`,
      lesson: '勇气不是不害怕，而是害怕时也愿意往前走一步。',
      object: '会发光的小口袋',
      friend: '圆耳朵小伙伴'
    },
    '分享': {
      title: name => `${name}和一块会变大的饼干`,
      lesson: '分享不是失去一半，而是让快乐多出一个人。',
      object: '会变大的饼干',
      friend: '背着小书包的朋友'
    },
    '睡觉': {
      title: name => `${name}的晚安小船`,
      lesson: '睡觉不是错过世界，而是让明天的自己充满电。',
      object: '会唱歌的晚安小船',
      friend: '月亮船长'
    },
    '自信': {
      title: name => `${name}的小小声音`,
      lesson: '声音不需要很大，只要是真的，也会被世界听见。',
      object: '会收集掌声的小铃铛',
      friend: '戴帽子的云朵'
    }
  };

  const scenes = ['home', 'forest', 'sea', 'night', 'forest', 'stage', 'home', 'night'];
  let currentBook = null;
  let currentPage = 0;
  let lastFocus = null;

  const getFormData = () => {
    const data = new FormData(form);
    return {
      childName: String(data.get('childName') || defaults.childName).trim().slice(0, 12) || defaults.childName,
      childAge: String(data.get('childAge') || defaults.childAge),
      childRole: String(data.get('childRole') || defaults.childRole),
      theme: String(data.get('theme') || defaults.theme),
      style: String(data.get('style') || defaults.style),
      traits: String(data.get('traits') || defaults.traits).trim() || defaults.traits,
      details: String(data.get('details') || defaults.details).trim() || defaults.details
    };
  };

  const setFormData = data => {
    Object.entries(data).forEach(([key, value]) => {
      const fields = form.elements[key];
      if (!fields) return;
      if (fields instanceof RadioNodeList) {
        Array.from(fields).forEach(field => {
          if (field.value === value) field.checked = true;
        });
      } else {
        fields.value = value;
      }
    });
  };

  const splitDetail = text => {
    const parts = text.split(/[、,，。；;]/).map(item => item.trim()).filter(Boolean);
    return {
      first: parts[0] || '一件最熟悉的小东西',
      second: parts[1] || '睡前最喜欢的角落'
    };
  };

  const buildBook = input => {
    const config = themeData[input.theme] || themeData['勇气'];
    const detail = splitDetail(input.details);
    const name = input.childName;
    const role = input.childRole;
    const title = config.title(name);
    const pages = [
      {
        heading: '封面',
        text: `${name}在${detail.second}旁边发现了${config.object}。它轻轻一闪，好像在说：“今晚，你就是故事的主角。”`,
        scene: 'home'
      },
      {
        heading: '小小问题出现了',
        text: `${name}${input.traits ? `是个${input.traits}的孩子` : '有很多奇妙的想法'}。可是今天，${role}遇到了一件不太容易的事。`,
        scene: 'forest'
      },
      {
        heading: '出发',
        text: `${config.friend}从书页里探出头，邀请${name}把${detail.first}带上。“我们不急，”小伙伴说，“一步一步来。”`,
        scene: 'sea'
      },
      {
        heading: '夜色里的声音',
        text: `路上有风声、树影和一点点不确定。${name}握紧${config.object}，发现它只有在${role}说出真实感受时才会发亮。`,
        scene: 'night'
      },
      {
        heading: '第一个办法',
        text: `${name}没有假装自己很厉害，而是认真想了一个小办法：先停下来，数三下，再请朋友一起试一次。`,
        scene: 'forest'
      },
      {
        heading: '大家都看见了',
        text: `当${name}把办法说出来，周围的小光点一颗一颗亮起。原来${input.theme}不是魔法，是愿意练习的小小动作。`,
        scene: 'stage'
      },
      {
        heading: '回到家',
        text: `${detail.first}安静地躺在桌上，${detail.second}也变得暖暖的。${name}知道，明天再遇到难题，${role}已经有办法开始。`,
        scene: 'home'
      },
      {
        heading: '给孩子的话',
        text: `${config.lesson} 亲爱的${name}，你不用一次就做到最好，只要愿意开始，你就已经在长大。`,
        scene: 'night'
      }
    ];

    return {
      title,
      subtitle: `${input.childAge} 岁孩子的${input.theme}主题绘本`,
      style: input.style,
      prompt: `画风：${input.style}。主角：${name}，${input.childAge}岁。特点：${input.traits}。真实细节：${input.details}。主题：${input.theme}。`,
      pages
    };
  };

  const renderThumbs = () => {
    if (!currentBook) return;
    thumbs.innerHTML = currentBook.pages.map((_, index) => (
      `<button class="thumb${index === currentPage ? ' is-active' : ''}" type="button" data-page="${index}" aria-label="查看第 ${index + 1} 页">${index + 1}</button>`
    )).join('');
  };

  const setStatus = message => {
    if (!saveStatus) return;
    saveStatus.textContent = message;
  };

  const renderPage = index => {
    if (!currentBook) return;
    const bounded = Math.max(0, Math.min(index, currentBook.pages.length - 1));
    currentPage = bounded;
    const page = currentBook.pages[bounded];
    titleEl.textContent = currentBook.title;
    pageNumber.textContent = `第 ${bounded + 1} 页 / ${currentBook.pages.length} 页`;
    pageHeading.textContent = page.heading;
    pageText.textContent = page.text;
    pageArt.dataset.scene = page.scene || scenes[bounded % scenes.length];
    renderThumbs();
    localStorage.setItem('huiben:lastBook', JSON.stringify({ book: currentBook, page: currentPage }));
  };

  const generate = () => {
    currentBook = buildBook(getFormData());
    renderPage(0);
    document.querySelector('.progress span:nth-child(2)')?.classList.add('is-active');
    setStatus('绘本已生成，可以阅读、打印或下载。');
  };

  const changePage = delta => {
    if (!currentBook) return;
    renderPage(currentPage + delta);
    if (reader.classList.contains('is-open')) renderReaderPage();
  };

  const renderReaderPage = () => {
    if (!currentBook) return;
    const page = currentBook.pages[currentPage];
    readerTitle.textContent = currentBook.title;
    readerPage.innerHTML = `
      <article class="book-page">
        <div class="page-art" data-scene="${page.scene || scenes[currentPage % scenes.length]}">
          <span class="sun"></span>
          <span class="path"></span>
          <span class="tree tree-left"></span>
          <span class="tree tree-right"></span>
          <span class="animal"></span>
        </div>
        <div class="page-copy">
          <span>第 ${currentPage + 1} 页 / ${currentBook.pages.length} 页</span>
          <h4>${page.heading}</h4>
          <p>${page.text}</p>
        </div>
      </article>
    `;
  };

  const openReader = () => {
    if (!currentBook) generate();
    lastFocus = document.activeElement;
    renderReaderPage();
    reader.classList.add('is-open');
    reader.setAttribute('aria-hidden', 'false');
    document.querySelector('.progress span:nth-child(3)')?.classList.add('is-active');
    reader.querySelector('[data-close-reader]')?.focus();
  };

  const closeReader = () => {
    reader.classList.remove('is-open');
    reader.setAttribute('aria-hidden', 'true');
    if (lastFocus && typeof lastFocus.focus === 'function') lastFocus.focus();
  };

  const downloadText = () => {
    if (!currentBook) generate();
    const lines = [
      currentBook.title,
      currentBook.subtitle,
      '',
      `插画提示：${currentBook.prompt}`,
      '',
      ...currentBook.pages.flatMap((page, index) => [
        `${index + 1}. ${page.heading}`,
        page.text,
        ''
      ])
    ];
    const blob = new Blob([lines.join('\n')], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `${currentBook.title}.txt`;
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
    setStatus('文本已生成，浏览器会开始下载。');
  };

  const restore = () => {
    try {
      const saved = JSON.parse(localStorage.getItem('huiben:lastBook') || 'null');
      if (saved?.book?.pages?.length) {
        currentBook = saved.book;
        renderPage(Number(saved.page || 0));
        return;
      }
    } catch {
      localStorage.removeItem('huiben:lastBook');
    }
    generate();
  };

  form.addEventListener('submit', event => {
    event.preventDefault();
    generate();
  });

  document.addEventListener('click', event => {
    const target = event.target.closest('button, a');
    if (!target) return;

    if (target.matches('[data-prev]')) changePage(-1);
    if (target.matches('[data-next]')) changePage(1);
    if (target.matches('.thumb')) renderPage(Number(target.dataset.page || 0));
    if (target.matches('[data-read]')) openReader();
    if (target.matches('[data-close-reader]')) closeReader();
    if (target.matches('[data-reader-prev]')) changePage(-1);
    if (target.matches('[data-reader-next]')) changePage(1);
    if (target.matches('[data-print]')) window.print();
    if (target.matches('[data-download]')) downloadText();
    if (target.matches('[data-reset]')) {
      setFormData(defaults);
      generate();
    }
    if (target.matches('[data-fill-demo]')) {
      setFormData(samples.friendship);
      generate();
      document.getElementById('workspace')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    if (target.matches('[data-sample]')) {
      const sample = samples[target.dataset.sample];
      if (sample) {
        setFormData(sample);
        generate();
        document.getElementById('workspace')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && reader.classList.contains('is-open')) closeReader();
    if (event.key === 'ArrowLeft') changePage(-1);
    if (event.key === 'ArrowRight') changePage(1);
  });

  window.addEventListener('load', () => {
    if (window.lucide) window.lucide.createIcons();
  });

  restore();
})();
