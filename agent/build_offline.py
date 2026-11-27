"""Package the deployed dashboard, technical training and SIRE questions for file://."""
from build_web import prepare
import argparse
import base64
import json
import re
from pathlib import Path

APP = Path(__file__).resolve().parents[1] / 'docs'


def embedded_icon(match):
    path = APP / match.group('path')
    encoded = base64.b64encode(path.read_bytes()).decode('ascii')
    return f'{match["attribute"]}="data:image/png;base64,{encoded}"'


def build(dest):
    html = prepare((APP / 'index.html').read_text(encoding='utf-8'))
    html = re.sub(r'<link rel="(?:manifest|apple-touch-icon)"[^>]*>', '', html)
    html = re.sub(r'(?P<attribute>href|src)="(?:\./)?(?P<path>icons/icon\d+\.png)"', embedded_icon, html)
    html = html.replace('<link rel="stylesheet" href="styles.css">',
                        '<style>' + (APP / 'styles.css').read_text() + '</style>')
    # The file is also usable on its first opening at sea, without a fetch.
    feed = json.loads((APP / 'data/intelligence.json').read_text(encoding='utf-8'))
    if feed.get('schema_version') != 1 or not isinstance(feed.get('entries'), list):
        raise ValueError('Invalid release feed')
    payload = json.dumps(feed, ensure_ascii=False, separators=(',', ':')).replace('<', r'\u003c')
    html, count = re.subn(r'^const RELEASE_REFERENCE = .*?;$',
                          lambda _: 'const RELEASE_REFERENCE = ' + payload + ';', html, flags=re.M)
    if count != 1:
        raise ValueError('Missing bundled reading edition')
    parts = []
    for name in ['p1a','p1b','p1c','p1d','p1e','p2a','p2b','p2c','p2d']:
        module = (APP / f'sire_{name}.js').read_text()
        parts.append(re.sub(r'^export (?=const )', '', module, flags=re.M))
    deck = (APP / 'sire_training.js').read_text().replace("import './sea_glass.js';\n", '')
    parts.append(re.sub(r"^import \{[^}]+\} from './sire_[^']+\.js';\s*", '', deck, flags=re.M))
    tag = '<script type="module" src="./sire_training.js"></script>'
    if html.count(tag) != 1:
        raise ValueError('Missing SIRE module entry point')
    code = '\n'.join(parts).replace('</script', '<\\/script')
    dest.write_text(html.replace(tag, '<script>(()=>{\n' + code + '\n})();</script>'), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=Path)
    build(parser.parse_args().output)
