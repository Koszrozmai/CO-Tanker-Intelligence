"""Prepare the GitHub Pages shell from the repository's technical-training edition."""
from pathlib import Path
import re

APP = Path(__file__).resolve().parents[1] / 'docs'


def prepare(html):
    if '<div class="sea-actions">' in html:
        return html
    html = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="styles.css">', html, count=1, flags=re.S)
    html = re.sub(r'href="data:image/png;base64,[^"]+"', 'href="icons/icon192.png"', html)
    html = html.replace('const localFile=true;', "const localFile=location.protocol==='file:' || new URLSearchParams(location.search).has('standalone');")
    html = html.replace('const isLocal=true;', "const isLocal=location.protocol==='file:';")
    html = html.replace('CO Tanker Intelligence · Offline', 'CO Tanker Intelligence').replace('#0a1322', '#143e49')
    html = re.sub(r'<div class="brand-icon">.*?</div>', '<img class="brand-icon" src="icons/icon128.png" width="40" height="40" alt="">', html, count=1)
    labels = {
        'OPEN MODULE':'Moduł', '>CO INTELLIGENCE<':'>CO Tanker<', '>TANKER REGULATORY WATCH<':'>Intelligence<',
        'Trening inspekcyjny i AI':'Biblioteka SIRE 2.0 i trening', ' Trening i AI</button>':' Biblioteka SIRE 2.0</button>',
        ' Refresh now</button>':' Odśwież</button>', '>Open Watch<':'>Aktualności<', '>Watch briefing<':'>Przegląd źródeł<',
        '>Command overview<':'>Pulpit<', "overview:'Command overview'":"overview:'Pulpit'",
        "practice:'Inspector practice & AI'":"practice:'Biblioteka SIRE 2.0'",
        'SIRE 2.0 — prawdziwe pytania i praktyczny trening':'Biblioteka SIRE 2.0',
        'v1.8 · Samsung / Android · PWA':'Sea Glass · PWA',
        'Samsung PWA · Offline inspection & Academy ready. Some public sites block direct browser fetches; enable a trusted server relay for the live news feed.':'Aktualności pochodzą z ostatniego przeglądu źródeł. Postęp treningu zapisuje się na tym urządzeniu.'
    }
    for old, new in labels.items():
        html = html.replace(old, new)
    html = re.sub(r'<div class="hero">.*?</div></div>', '', html, count=1, flags=re.S)
    actions = ('<div class="sea-actions"><a class="button-primary" href="#practice">Trening SIRE 2.0</a>'
               '<button class="button-outline" data-action="open-feed">Archiwum informacji</button>'
               '<button class="button-outline" data-action="open-learning">Baza wiedzy</button></div>')
    marker = '<div class="glass-card watch-overview">'
    if marker not in html:
        raise ValueError('Missing briefing entry point')
    return html.replace(marker, actions + marker, 1)


if __name__ == '__main__':
    index = APP / 'index.html'
    index.write_text(prepare(index.read_text()), encoding='utf-8')
