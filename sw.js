/**
 * Service Worker for Just Jason Blog
 * 提供离线访问和资源缓存功能
 */

const CACHE_VERSION = 'v1.0.0';
const CACHE_NAME = `just-jason-${CACHE_VERSION}`;

// 需要预缓存的核心资源
const PRECACHE_ASSETS = [
  '/',
  '/assets/css/main.css',
  '/assets/css/theme.min.css',
  '/assets/css/dark-mode.css',
  '/assets/js/theme.min.js',
  '/assets/images/favicon/apple-touch-icon.png',
  '/assets/images/favicon/favicon-32x32.png',
  '/assets/images/logo.png',
  '/offline.html'
];

// 需要缓存的资源类型
const CACHEABLE_TYPES = [
  'style',
  'script',
  'image',
  'font'
];

// 安装事件 - 预缓存核心资源
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('[SW] Precaching core assets');
        return cache.addAll(PRECACHE_ASSETS.filter(url => {
          // 只缓存存在的资源，忽略错误
          return true;
        }));
      })
      .then(() => self.skipWaiting())
      .catch(err => {
        console.log('[SW] Precache failed:', err);
        return self.skipWaiting();
      })
  );
});

// 激活事件 - 清理旧缓存
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames
            .filter(cacheName => cacheName.startsWith('just-jason-') && cacheName !== CACHE_NAME)
            .map(cacheName => {
              console.log('[SW] Deleting old cache:', cacheName);
              return caches.delete(cacheName);
            })
        );
      })
      .then(() => self.clients.claim())
  );
});

// 请求拦截 - 缓存策略
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  // 只处理同源请求和 GET 请求
  if (request.method !== 'GET' || url.origin !== location.origin) {
    return;
  }

  // 跳过 Chrome 扩展和其他特殊协议
  if (url.protocol !== 'http:' && url.protocol !== 'https:') {
    return;
  }

  // HTML 页面 - Network First 策略
  if (request.destination === 'document' || request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      fetch(request)
        .then(response => {
          // 缓存成功的响应
          if (response.ok) {
            const responseClone = response.clone();
            caches.open(CACHE_NAME).then(cache => {
              cache.put(request, responseClone);
            });
          }
          return response;
        })
        .catch(() => {
          // 网络失败时从缓存获取
          return caches.match(request)
            .then(cachedResponse => {
              if (cachedResponse) {
                return cachedResponse;
              }
              // 返回离线页面
              return caches.match('/offline.html');
            });
        })
    );
    return;
  }

  // 静态资源 - Cache First 策略
  if (CACHEABLE_TYPES.includes(request.destination)) {
    event.respondWith(
      caches.match(request)
        .then(cachedResponse => {
          if (cachedResponse) {
            // 后台更新缓存
            fetch(request).then(response => {
              if (response.ok) {
                caches.open(CACHE_NAME).then(cache => {
                  cache.put(request, response);
                });
              }
            }).catch(() => {});
            return cachedResponse;
          }

          // 缓存未命中，从网络获取
          return fetch(request)
            .then(response => {
              if (response.ok) {
                const responseClone = response.clone();
                caches.open(CACHE_NAME).then(cache => {
                  cache.put(request, responseClone);
                });
              }
              return response;
            });
        })
    );
    return;
  }

  // 其他请求 - 默认网络优先
  event.respondWith(
    fetch(request)
      .catch(() => caches.match(request))
  );
});

// 后台同步 (如果支持)
self.addEventListener('sync', event => {
  if (event.tag === 'sync-posts') {
    console.log('[SW] Background sync triggered');
  }
});

// 消息处理
self.addEventListener('message', event => {
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
  }

  if (event.data === 'clearCache') {
    caches.delete(CACHE_NAME).then(() => {
      console.log('[SW] Cache cleared');
    });
  }
});
