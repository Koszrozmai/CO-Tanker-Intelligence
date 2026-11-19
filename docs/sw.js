const PREFIX='co-tanker-intelligence-';
const CACHE=PREFIX+'v1.8.1';
const ROOT=new URL('./',self.registration.scope);
const ASSETS=['./','./index.html','./manifest.webmanifest','./icons/icon192.png','./icons/icon512.png'];
const paths=new Set(ASSETS.map(p=>new URL(p,ROOT).pathname));
self.addEventListener('install',event=>event.waitUntil((async()=>{
 const cache=await caches.open(CACHE);
 await cache.addAll(ASSETS.map(p=>new Request(new URL(p,ROOT),{cache:'reload',redirect:'error'})));
 await self.skipWaiting();
})()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{
 for(const name of await caches.keys())if(name.startsWith(PREFIX)&&name!==CACHE)await caches.delete(name);
 await self.clients.claim();
})()));
self.addEventListener('fetch',event=>{
 if(event.request.method!=='GET')return;
 const url=new URL(event.request.url);
 if(url.origin!==ROOT.origin||!paths.has(url.pathname))return;
 event.respondWith((async()=>{
  const cache=await caches.open(CACHE),key=new URL(url.pathname,ROOT);
  return await cache.match(key)||fetch(event.request);
 })());
});