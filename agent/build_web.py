"""Prepare the GitHub Pages shell from the repository's technical-training edition."""
from pathlib import Path
import re

APP = Path(__file__).resolve().parents[1] / 'docs'

def embed_current_watch(html):
    """Replace stale Watch JS in the monolithic HTML with the maintained source."""
    src = (APP / 'always_on_ui.js').read_text(encoding='utf-8')
    src = re.sub(r"^import \{RELEASE_REFERENCE\} from './release_reference.js';\s*", "", src, count=1)
    src = re.sub(r"^export (?=(?:function|const|let|class)\b)", "", src, flags=re.M)
    wrapper = ("modules['always_on_ui']=(()=>{\n"
               "const {RELEASE_REFERENCE}=modules['release_reference'];\n"
               + src.rstrip() + "\n"
               "return {exportWatchBackup,importWatchBackup,onWatchPage,wireWatch};\n"
               "})();")
    match = re.search(r"modules\['always_on_ui'\]=\(\(\)=>\{.*?\n\}\)\(\);(?=\nmodules\['training_ui'\])",html,flags=re.S)
    if not match:
        raise ValueError('Bundled Watch module marker not found — refusing stale deployment')
    html = html[:match.start()] + wrapper + html[match.end():]
    if "provenanceLabel(e)" not in html:
        raise ValueError('New provenance UI not included in Watch bundle')
    return html



def prepare(html):
    if '<div class="sea-actions">' in html:
        return embed_current_watch(html)
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
    html = html.replace('<option value="all">All publications</option>',
        '<option value="all">Wszystkie publikacje</option>'
        '<option value="regulator">Oficjalne</option>'
        '<option value="industry_body">Organizacje branżowe</option>'
        '<option value="editorial">Media branżowe</option>'
        '<option value="social">YouTube / Social</option>', 1)
    html = html.replace('id="watchSaveUrl">Connect feed</button>',
       'id="watchSaveUrl">Połącz</button><button class="button-outline small" id="watchUseGithub">Przywróć aktualności GitHub</button>', 1)
    html = html.replace('Source health and last successful checks', 'Dostępność źródeł i ostatnie poprawne odczyty')
    html = html.replace('Source, topic or title', 'Wydawca, temat lub tytuł')
    html = re.sub(r'<div class="hero">.*?(?=<div class="metrics">)', '', html, count=1, flags=re.S)
    actions = ('<div class="sea-actions"><a class="button-primary" href="#watch">Aktualności i źródła</a>'
               '<a class="button-outline" href="#technical">Technika i szkolenia</a>'
               '<a class="button-outline" href="#practice">Trening SIRE 2.0</a></div>')
    marker = '<div class="glass-card watch-overview">'
    if marker not in html:
        raise ValueError('Missing briefing entry point')
    return embed_current_watch(html.replace(marker, actions + marker, 1))


if __name__ == '__main__':
    index = APP / 'index.html'
    index.write_text(prepare(index.read_text()), encoding='utf-8')
