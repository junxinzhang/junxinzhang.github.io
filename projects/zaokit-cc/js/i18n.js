/**
 * Zaokit CC — Internationalisation (i18n)
 *
 * Auto-detects browser language (zh-* → zh, else → en).
 * Persists choice in localStorage. Walks DOM for [data-i18n] attributes.
 */

const I18N = (() => {
  const locales = {
    zh: {
      'meta.title': 'Zaokit Claude API 服务 - 企业级稳定接入方案',
      'meta.description': 'Zaokit 提供企业级 Claude API 接入服务。支持 Claude 最新全系列模型，高并发、高可用，100% 兼容官方接口，支持企业合同与正式 Invoice。',

      'skip': '跳到正文',
      'brand.aria': 'Zaokit 主页',
      'menu.aria': '打开导航菜单',

      'nav.home': '首页',
      'nav.advantages': '核心优势',
      'nav.pricing': '计费方案',
      'nav.features': '功能特性',
      'nav.process': '接入流程',
      'nav.faq': '常见问题',

      'hero.eyebrow': '企业级 Claude API 接入',
      'hero.h1.line1': '解锁 Claude 的强大能力，',
      'hero.h1.line2': '让 AI 稳定服务于业务。',
      'hero.desc': 'Zaokit 为企业提供高性能、高可用的 Claude API 接入服务。100% 兼容官方接口协议，支持全系列模型，支持签订企业合同并出具正式 Invoice。',
      'hero.cta.primary': '联系客户经理',
      'hero.cta.secondary': '查看计费方案',
      'hero.meta.invoice': '支持企业合同与正式 Invoice',
      'hero.meta.models': '包含 Claude 最新全系列模型',

      'hero.card.title': '为什么企业选择我们',
      'hero.card.1.title': '清晰透明的商务流程',
      'hero.card.1.desc': '签订正式服务合同，企业账户付款，出具正式 Invoice，方便采购审批与财务入账。',
      'hero.card.2.title': '原生级别的开发体验',
      'hero.card.2.desc': 'API 请求结构与 Anthropic 官方完全一致，只需修改 Base URL 即可无缝切换，无需重写现有代码。',
      'hero.card.3.title': '企业级的稳定保障',
      'hero.card.3.desc': '多重路由、并发隔离池与故障转移机制，保障高频调用场景下的极速响应与可用性。',

      'stat.sla.label': 'SLA 承诺可用性',
      'stat.latency.label': '首字响应延迟',
      'stat.compat.label': 'API 兼容性',
      'stat.support.label': '技术支持响应',

      'adv.tag': '核心优势',
      'adv.title': '专为 B2B 场景打造的接入体验',
      'adv.1.title': '透明的商务流程',
      'adv.1.desc': '支持先签订服务合同再付款，企业银行转账结算，按实际抬头出具正式 Invoice，方便企业采购与财务入账。',
      'adv.2.title': '低延迟的稳定网络层',
      'adv.2.desc': '多线路智能路由与自动故障转移，配合并发隔离调度，有效降低高峰期请求失败率。',
      'adv.3.title': '数据安全与隐私',
      'adv.3.desc': '作为透明转发层，我们坚守不记录、不缓存任何 prompt 及生成内容的底线。您的所有对话数据直达模型厂商，满足企业级隐私要求。',

      'pricing.tag': '计费方案',
      'pricing.title': '透明、灵活的充值模式',
      'pricing.desc': '按 Token 消耗实时计费，无隐形费用，无月租，充值金额永不过期。',
      'pricing.basic.name': '基础起步',
      'pricing.basic.price': '$149',
      'pricing.basic.unit': ' /次',
      'pricing.basic.note': '适合小型团队与测试验证',
      'pricing.basic.f1': '按实际 Token 消耗扣费',
      'pricing.basic.f2': '提供正式 Invoice',
      'pricing.basic.f3': '基础并发配额',
      'pricing.basic.f4': '工作日邮件支持',
      'pricing.basic.btn': '选择方案',
      'pricing.std.badge': '最受欢迎',
      'pricing.std.name': '企业标准',
      'pricing.std.price': '$749',
      'pricing.std.unit': ' /次',
      'pricing.std.note': '适合规模化生产环境部署',
      'pricing.std.f1': '按实际 Token 消耗扣费',
      'pricing.std.f2': '提供正式 Invoice',
      'pricing.std.f3': '专属高并发独立通道',
      'pricing.std.f4': '优先技术支持响应',
      'pricing.std.f5': '专属客户经理跟进',
      'pricing.std.btn': '联系采购',
      'pricing.ent.name': '定制大客户',
      'pricing.ent.price': '$2,999+',
      'pricing.ent.note': '超大并发与特殊业务需求',
      'pricing.ent.f1': '阶梯优惠折扣费率',
      'pricing.ent.f2': '签订年度框架协议',
      'pricing.ent.f3': '独占资源配置',
      'pricing.ent.f4': '7x24 小时紧急响应',
      'pricing.ent.f5': '技术专家驻场支持可选',
      'pricing.ent.btn': '定制方案',

      'process.tag': '接入流程',
      'process.title': '4 步完成接入',
      'process.1.title': '1. 需求确认与测试',
      'process.1.desc': '联系我们提供基本业务场景，获取少量免费测试额度和接口文档，验证兼容性与速度。',
      'process.2.title': '2. 商务合同签署',
      'process.2.desc': '确认采购方案后，双方签署服务合同，明确服务等级、付款与发票细节。',
      'process.3.title': '3. 付款与发票',
      'process.3.desc': '企业银行转账付款，到账确认后我们出具正式 Invoice 电子版。',
      'process.4.title': '4. 获取 Key 并上线',
      'process.4.desc': '发放正式生产环境的 API Key 和专属 Endpoint，您的系统即可稳定调用大模型能力。',

      'features.tag': '功能特性',
      'features.title': '专为开发者与工程团队准备',
      'features.f1': '支持 Claude 最新全系列模型',
      'features.f2': '完美支持 Server-Sent Events (SSE) 流式输出响应',
      'features.f3': '支持 Function Calling (工具调用) 与 Vision 多模态输入',
      'features.f4': '通过统一计费面板实时监控 Token 消耗及账单情况',
      'features.f5': '支持 LangChain / LlamaIndex 等主流开发框架无缝集成',
      'features.f6': '接口级防重放攻击与基础 CC 防护',
      'features.panel.title': '极简的代码集成',
      'features.panel.desc': '如果您已经在使用官方 SDK（如 Python 或 Node.js），只需一行代码将 Base URL 修改为我们提供的 Endpoint 即可：',
      'features.panel.note': '无任何学习成本，即插即用。',

      'faq.tag': 'FAQ',
      'faq.title': '常见问题解答',
      'faq.1.q': 'Q1：你们的计费标准和官方一样吗？',
      'faq.1.a': '我们按照模型官方公开的 Token 定价进行计算，由于需要承担基础设施、多线路容灾与运维服务成本，综合费率会有一定的溢价。具体报价请联系客户经理获取最新的阶梯价格表。',
      'faq.2.q': 'Q2：支持 OpenAI 的 ChatGPT 接口吗？',
      'faq.2.a': '支持。我们同样提供 OpenAI 全系列模型（如 GPT-4o, GPT-4-turbo, o1 等）的接入服务，且共用同一套额度和计费系统，让您的多模型混用策略更易管理。',
      'faq.3.q': 'Q3：调用会有并发（RPM/TPM）限制吗？',
      'faq.3.a': '基础方案会有软性的并发限流机制以保障整体稳定性。企业级客户可分配专属资源与独立通道，满足高并发生产环境需求。',
      'faq.4.q': 'Q4：服务出现异常时，我的余额怎么办？',
      'faq.4.a': '账户余额长期有效。我们通过多线路冗余与故障转移保障服务连续性，如遇异常会第一时间处理，期间您的余额不受任何影响。',

      'cta.title': '准备好为您的企业引入顶级 AI 能力了吗？',
      'cta.desc': '告诉我们您的业务场景，立即获取测试额度及专属采购方案。',
      'cta.email': '发送邮件咨询',

      'footer.brand': 'Zaokit AI Services',
      'footer.note': '专注为全球企业提供安全、稳定的顶尖 AI 大模型 API 接入方案。',
      'footer.nav': '快速导航',
      'footer.nav.adv': '核心优势',
      'footer.nav.pricing': '计费方案',
      'footer.nav.features': '功能特性',
      'footer.nav.faq': '常见问题',
      'footer.contact': '联系我们',
      'footer.hours': '工作时间：周一至周五 10:00 - 19:00（UTC+8）',
      'footer.related': '相关产品',
      'footer.related.th': 'AI Token Hub · 企业算力总闸',
      'footer.related.cx': 'Zaokit CX · Codex API 服务',
      'footer.related.app': 'Zaokit · AI 创作入口',

      'lang.label': 'EN',
    },

    en: {
      'meta.title': 'Zaokit Claude API — Enterprise-Grade, Reliable Access',
      'meta.description': 'Zaokit provides enterprise-grade Claude API access. Supporting the latest Claude models with high concurrency and availability, 100% compatible with the official API, with business contracts and formal invoices.',

      'skip': 'Skip to content',
      'brand.aria': 'Zaokit Home',
      'menu.aria': 'Open navigation menu',

      'nav.home': 'Home',
      'nav.advantages': 'Advantages',
      'nav.pricing': 'Pricing',
      'nav.features': 'Features',
      'nav.process': 'Get Started',
      'nav.faq': 'FAQ',

      'hero.eyebrow': 'Enterprise Claude API Access',
      'hero.h1.line1': 'Unlock the power of Claude,',
      'hero.h1.line2': 'reliably powering your business.',
      'hero.desc': 'Zaokit provides high-performance, highly available Claude API access for enterprises. 100% compatible with the official Anthropic protocol, supporting the full model lineup, with business contracts and formal invoices.',
      'hero.cta.primary': 'Contact Sales',
      'hero.cta.secondary': 'View Pricing',
      'hero.meta.invoice': 'Business contracts & formal invoices',
      'hero.meta.models': 'Latest Claude Opus / Sonnet / Haiku',

      'hero.card.title': 'Why enterprises choose us',
      'hero.card.1.title': 'Clear, transparent procurement',
      'hero.card.1.desc': 'Sign a formal service contract, pay from your company account, and receive a formal invoice — easy for procurement and accounting.',
      'hero.card.2.title': 'Native-level developer experience',
      'hero.card.2.desc': 'API request structure is 100% identical to official Anthropic. Just change the Base URL to switch over — no code rewrite needed.',
      'hero.card.3.title': 'Enterprise-grade reliability',
      'hero.card.3.desc': 'Multi-route failover, isolated concurrency pools, and automatic traffic rerouting ensure ultra-fast response and high availability under heavy loads.',

      'stat.sla.label': 'SLA uptime guarantee',
      'stat.latency.label': 'Time to first token',
      'stat.compat.label': 'API compatibility',
      'stat.support.label': 'Support response',

      'adv.tag': 'Advantages',
      'adv.title': 'Built for B2B scenarios',
      'adv.1.title': 'Transparent procurement',
      'adv.1.desc': 'Sign a service contract before paying, settle by corporate bank transfer, and receive formal invoices under your company name — easy for procurement and accounting.',
      'adv.2.title': 'Low-latency, reliable network layer',
      'adv.2.desc': 'Multi-route intelligent routing with automatic failover and isolated concurrency scheduling keeps request failures low even at peak load.',
      'adv.3.title': 'Data security & privacy',
      'adv.3.desc': 'As a transparent forwarding layer, we never log or cache any prompts or generated content. All conversation data goes directly to the model provider, meeting enterprise privacy requirements.',

      'pricing.tag': 'Pricing',
      'pricing.title': 'Transparent, flexible top-up model',
      'pricing.desc': 'Pay-as-you-go by token consumption. No hidden fees, no monthly subscription, credits never expire.',
      'pricing.basic.name': 'Starter',
      'pricing.basic.price': '$149',
      'pricing.basic.unit': ' /top-up',
      'pricing.basic.note': 'For small teams & testing',
      'pricing.basic.f1': 'Pay by actual token consumption',
      'pricing.basic.f2': 'Formal invoice',
      'pricing.basic.f3': 'Basic concurrency quota',
      'pricing.basic.f4': 'Weekday email support',
      'pricing.basic.btn': 'Choose Plan',
      'pricing.std.badge': 'Most Popular',
      'pricing.std.name': 'Enterprise Standard',
      'pricing.std.price': '$749',
      'pricing.std.unit': ' /top-up',
      'pricing.std.note': 'For production environments at scale',
      'pricing.std.f1': 'Pay by actual token consumption',
      'pricing.std.f2': 'Formal invoice',
      'pricing.std.f3': 'Dedicated high-concurrency channel',
      'pricing.std.f4': 'Priority technical support',
      'pricing.std.f5': 'Dedicated account manager',
      'pricing.std.btn': 'Contact Sales',
      'pricing.ent.name': 'Custom Enterprise',
      'pricing.ent.price': '$2,999+',
      'pricing.ent.note': 'Ultra-high concurrency & special needs',
      'pricing.ent.f1': 'Volume discount tiers',
      'pricing.ent.f2': 'Annual framework agreement',
      'pricing.ent.f3': 'Dedicated resource allocation',
      'pricing.ent.f4': '7×24 emergency response',
      'pricing.ent.f5': 'Optional on-site tech expert',
      'pricing.ent.btn': 'Custom Plan',

      'process.tag': 'Get Started',
      'process.title': '4 steps to get started',
      'process.1.title': '1. Requirements & Testing',
      'process.1.desc': 'Contact us with your business scenario. Get free test credits and API docs to verify compatibility and speed.',
      'process.2.title': '2. Sign Contract',
      'process.2.desc': 'Once the plan is confirmed, both parties sign a service contract with SLA, payment and invoicing details clearly defined.',
      'process.3.title': '3. Payment & Invoicing',
      'process.3.desc': 'Pay by corporate bank transfer. Upon confirmation, we issue a formal invoice electronically.',
      'process.4.title': '4. Get Your Key & Go Live',
      'process.4.desc': 'Receive your production API Key and dedicated endpoint. Your system can now stably call LLM capabilities.',

      'features.tag': 'Features',
      'features.title': 'Built for developers & engineering teams',
      'features.f1': 'Latest Claude model lineup',
      'features.f2': 'Full Server-Sent Events (SSE) streaming support',
      'features.f3': 'Function Calling (tool use) & Vision multimodal input',
      'features.f4': 'Real-time token consumption & billing dashboard',
      'features.f5': 'Seamless LangChain / LlamaIndex integration',
      'features.f6': 'API-level replay protection & basic CC defense',
      'features.panel.title': 'Dead-simple code integration',
      'features.panel.desc': 'If you\'re already using the official SDK (Python or Node.js), just change the Base URL to our endpoint:',
      'features.panel.note': 'Zero learning curve. Plug and play.',

      'faq.tag': 'FAQ',
      'faq.title': 'Frequently Asked Questions',
      'faq.1.q': 'Q1: Is your pricing the same as the official rates?',
      'faq.1.a': 'We calculate based on the model\'s official published token pricing. Due to infrastructure, multi-route redundancy and operations costs, there is a modest premium. Contact your account manager for the latest tiered pricing.',
      'faq.2.q': 'Q2: Do you support OpenAI\'s ChatGPT APIs?',
      'faq.2.a': 'Yes. We also provide access to the full OpenAI model lineup (GPT-4o, GPT-4-turbo, o1, etc.), sharing the same credits and billing system, making multi-model strategies easier to manage.',
      'faq.3.q': 'Q3: Are there concurrency (RPM/TPM) limits?',
      'faq.3.a': 'The Starter plan has soft rate-limiting to ensure overall stability. Enterprise clients can get dedicated resources and isolated channels for high-concurrency production workloads.',
      'faq.4.q': 'Q4: What happens to my balance if the service has an issue?',
      'faq.4.a': 'Your balance never expires. Multi-route redundancy and failover keep the service running, any incident is handled immediately, and your balance is never affected.',

      'cta.title': 'Ready to bring top-tier AI to your enterprise?',
      'cta.desc': 'Tell us about your use case and get test credits and a tailored procurement plan today.',
      'cta.email': 'Send Email',

      'footer.brand': 'Zaokit AI Services',
      'footer.note': 'Providing secure, stable access to the world\'s leading AI model APIs for enterprises worldwide.',
      'footer.nav': 'Quick Links',
      'footer.nav.adv': 'Advantages',
      'footer.nav.pricing': 'Pricing',
      'footer.nav.features': 'Features',
      'footer.nav.faq': 'FAQ',
      'footer.contact': 'Contact',
      'footer.hours': 'Hours: Mon–Fri 10:00–19:00 (UTC+8)',
      'footer.related': 'Related Products',
      'footer.related.th': 'AI Token Hub · Compute Management',
      'footer.related.cx': 'Zaokit CX · Codex API Service',
      'footer.related.app': 'Zaokit · AI Creation Portal',

      'lang.label': '中文',
    },
  };

  const STORAGE_KEY = 'zaokit_cc_lang';
  let currentLang = 'zh';

  function detectLang() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved && locales[saved]) return saved;
    const nav = (navigator.language || navigator.userLanguage || '').toLowerCase();
    return nav.startsWith('zh') ? 'zh' : 'en';
  }

  function t(key) {
    return (locales[currentLang] && locales[currentLang][key]) || (locales.zh[key]) || key;
  }

  function applyTranslations() {
    document.querySelectorAll('[data-i18n]').forEach((el) => {
      el.textContent = t(el.dataset.i18n);
    });
    document.querySelectorAll('[data-i18n-aria]').forEach((el) => {
      el.setAttribute('aria-label', t(el.dataset.i18nAria));
    });
    document.title = t('meta.title');
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.setAttribute('content', t('meta.description'));
    document.documentElement.lang = currentLang === 'zh' ? 'zh-CN' : 'en';
    const langBtn = document.getElementById('lang-switch');
    if (langBtn) langBtn.textContent = t('lang.label');
  }

  function init() {
    currentLang = detectLang();
    applyTranslations();
  }

  function switchLang() {
    currentLang = currentLang === 'zh' ? 'en' : 'zh';
    localStorage.setItem(STORAGE_KEY, currentLang);
    applyTranslations();
  }

  function getLang() { return currentLang; }

  return { init, switchLang, getLang, t };
})();
