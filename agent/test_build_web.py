import unittest
from pathlib import Path
from build_web import APP, prepare

class PublishedAppTests(unittest.TestCase):
    def test_pages_bundle_uses_current_watch_code(self):
        html=prepare((APP/'index.html').read_text(encoding='utf-8'))
        self.assertIn('function provenanceLabel(e)',html)
        self.assertIn('watchUseGithub',html)
        self.assertIn('watchProvenance',html) if 'watchProvenance' in html else self.assertIn('watch-provenance',html)
        self.assertNotIn('const localFile=true;',html)
        self.assertIn('value="editorial"',html)
        self.assertIn('value="social"',html)
        self.assertIn("modules['always_on_ui']",html)
        self.assertIn('sireDeckTrainer',html)
    def test_build_idempotent(self):
        html=prepare((APP/'index.html').read_text(encoding='utf-8'))
        self.assertEqual(prepare(html),html)

if __name__=='__main__':unittest.main()
