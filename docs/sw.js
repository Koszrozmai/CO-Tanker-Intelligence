/* CO Tanker Intelligence v1.9.0 - offline-first, update-aware app shell */
const CACHE='co-tanker-intelligence-v1.9.0';
const ROOT=new URL('./',self.registration.scope);
const PATHS=['./','./index.html','./manifest.webmanifest','./icons/icon192.png','./icons/icon512.png'];
const SET=new Set(PATHS.map(p=>new URL(p,ROOT).pathname));
self.addEventListener('install',event=>event.waitUntil((async()=>{
 const cache=await caches.open(CACHE);
 await cache.addAll(PATHS.map(p=>new Request(new URL(p,ROOT),{cache:'reload',credentials:'same-origin'})));
 await self.skipWaiting();
})()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{
 for(const key of await caches.keys())if(key.startsWith('co-tanker-intelligence-')&&key!==CACHE)await caches.delete(key);
 await self.clients.claim();
})()));
self.addEventListener('fetch',event=>{
 const url=new URL(event.request.url);
 if(event.request.method!=='GET'||url.origin!==ROOT.origin||!SET.has(url.pathname))return;
 event.respondWith((async()=>{
  const cache=await caches.open(CACHE);
  // Online uses the latest UI. Offline uses the installed app shell.
  if(event.request.mode==='navigate'||url.pathname===new URL('./index.html',ROOT).pathname||url.pathname===ROOT.pathname){
   try{
    const response=await fetch(event.request,{cache:'no-cache'});
    if(response.ok)await cache.put(event.request,response.clone());
    return response;
   }catch{
    return await cache.match(event.request,{ignoreSearch:true})||await cache.match(new URL('./index.html',ROOT));
   }
  }
  return await cache.match(event.request,{ignoreSearch:true})||fetch(event.request);
 })());
});