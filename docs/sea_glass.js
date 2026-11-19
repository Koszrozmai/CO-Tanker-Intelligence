// Upgrade legacy single-file Pages installations when the trainer module loads.
const overview = document.querySelector('#page-overview');
if (overview && !overview.querySelector('.sea-actions')) {
  const sheet = document.createElement('link');
  sheet.rel = 'stylesheet';
  sheet.href = './styles.css';
  document.head.append(sheet);
  const icon = document.createElement('img');
  icon.className = 'brand-icon';
  icon.src = './icons/icon128.png';
  icon.alt = '';
  document.querySelector('.brand-icon')?.replaceWith(icon);
  document.querySelector('link[rel="icon"]').href = './icons/icon192.png';
  document.querySelector('meta[name="theme-color"]').content = '#143e49';
  document.title = 'CO Tanker Intelligence';
  const actions = document.createElement('div');
  actions.className = 'sea-actions';
  const trainer = document.createElement('a');
  trainer.href = '#practice';
  trainer.className = 'button-primary';
  trainer.textContent = 'Trening SIRE 2.0';
  actions.append(trainer);
  // Move existing controls so their click handlers survive the layout change.
  actions.append(...overview.querySelectorAll('.hero-buttons button'));
  overview.querySelector('.hero')?.remove();
  overview.prepend(actions);
  if (location.protocol === 'https:') {
    const hint = document.getElementById('mobileHint');
    hint.textContent = 'Postęp treningu zapisuje się na tym urządzeniu.';
    const url = document.getElementById('watchFeedUrl');
    if (!url.value && !new URLSearchParams(location.search).has('standalone')) {
      url.value = './data/intelligence.json';
      document.getElementById('watchSaveUrl').click();
    }
    navigator.serviceWorker?.register('./sw.js').catch(() => {
      hint.textContent += ' Pamięć offline aplikacji jest niedostępna.';
    });
  }
}
