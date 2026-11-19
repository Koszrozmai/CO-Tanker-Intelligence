"""Regression checks for SIRE 2.0 deck training, UI, imports and legacy retention."""
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
NAMES=['p1a','p1b','p1c','p1d','p1e','p2a','p2b','p2c','p2d']
REQUIRED={'2.1.1','4.2.1','5.5.1','6.1.1','8.1.1','8.2.1','8.99.1','9.1.1','11.1.40','12.6.1'}
CLASS={'both','chemical','oil'}
AREA={'general','navigation','safety','pollution','security','cargo','mooring','photos','ice'}
class TestSireDeck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=[]
        for key in NAMES:
            doc=(ROOT/'docs'/f'sire_{key}.js').read_text(encoding='utf-8')
            match=re.search(r'^export const SIRE_'+key.upper()+r'=(\[.*\]);$',doc,re.M)
            assert match, f'{key}: missing exported data array'
            cls.rows+=json.loads(match.group(1))

    def test_scope_and_count(self):
        self.assertGreaterEqual(len(self.rows),250)
        ids=[x[0] for x in self.rows]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertTrue(REQUIRED.issubset(set(ids)), REQUIRED-set(ids))
        self.assertTrue(all(len(x)==10 for x in self.rows))
        self.assertTrue(all(x[3] in CLASS and x[4] in AREA for x in self.rows))
        self.assertFalse(any(x[0].startswith('10.') or x[0].startswith('8.4.') or x[0].startswith('8.5.') or x[0].startswith('8.6.') for x in self.rows))
        self.assertFalse(any('main engine' in x[1].lower() or 'purifier room' in x[1].lower() for x in self.rows))
        for x in self.rows:
            self.assertTrue(x[1].strip(),x[0])
            if x[4]!='photos':
                self.assertTrue(x[6].strip() and x[7].strip(),x[0])

    def test_web_and_extension_keep_all_original_modules(self):
        for path in [ROOT/'docs'/'index.html',ROOT/'Windows_Chrome'/'dashboard.html']:
            with self.subTest(path=path):
                html=path.read_text(encoding='utf-8')
                self.assertEqual(html.count('id="sireDeckTrainer"'),1)
                self.assertIn('src="./sire_training.js"',html)
                for key in ('sireStats','sireSearch','sireChapter','sireVessel','sireList','sireDetail','sireNext','sireExport'):
                    self.assertIn('id="'+key+'"',html)
                for legacy in ('id="practiceQueue"','id="practiceFilter"','id="referencesDesk"','id="copyAsk"'):
                    self.assertIn(legacy,html)
                self.assertIn('id="navMore"',html)
                self.assertEqual(html.count('data-page='),10)

    def test_module_dependencies_and_offline_cache(self):
        for root in [ROOT/'docs',ROOT/'Windows_Chrome']:
            s=(root/'sire_training.js').read_text(encoding='utf-8')
            self.assertIn('SIRE_DECK_BACKUP',s)
            self.assertIn('SIRE_DECK_IMPORT',s)
            self.assertIn('localStorage',s)
            self.assertIn('https://www.ocimf.org/programmes/sire-2-0/',s)
            for name in NAMES:
                self.assertIn(f"from './sire_{name}.js'",s)
                self.assertTrue((root/f'sire_{name}.js').is_file())
        sw=(ROOT/'docs'/'sw.js').read_text(encoding='utf-8')
        self.assertIn("'./sire_training.js'",sw)
        for name in NAMES:self.assertIn(f"'./sire_{name}.js'",sw)
        builder=(ROOT/'agent'/'build_offline.py').read_text(encoding='utf-8')
        self.assertIn("sire_training.js",builder)
        self.assertIn("for name in ['p1a'",builder)

if __name__=='__main__':
    unittest.main()
