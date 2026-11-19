"""Static regression checks for v1.9 compact UI and retained features."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "docs" / "index.html"
CHROME = ROOT / "Windows_Chrome" / "dashboard.html"
REQUIRED = (
    "overview", "watch", "feed", "saved", "inspections",
    "academy", "practice", "learning", "sources",
)
FIELDS = (
    "mobileJump", "watchFilter", "watchSearch", "watchMarkAll",
    "watchEntries", "watchLessons", "watchRefresh", "watchFeedUrl",
    "watchSaveUrl", "refreshBtn", "navUnread",
)

class TestCompactUI(unittest.TestCase):
    def test_all_modules_retained(self):
        for path, expert in ((WEB, "technical"), (CHROME, "planner")):
            with self.subTest(path=path):
                html = path.read_text(encoding="utf-8")
                nav = re.search(r'<nav class="main-nav"[^>]*>(.*?)</nav>', html, re.S)
                self.assertIsNotNone(nav)
                menu = re.findall(r'data-page="([^"]+)"', nav.group(1))
                self.assertEqual(set(menu), set(REQUIRED) | {expert})
                self.assertEqual(len(menu), 10)
                for name in menu:
                    self.assertIn(f'<option value="{name}">', html)
                self.assertIn('id="navMore"', html)
                self.assertIn('class="dashboard-more"', html)
                for field in FIELDS:
                    self.assertIn(f'id="{field}"', html)
    def test_mobile_has_one_navigation(self):
        css = (ROOT/"docs"/"styles.css").read_text(encoding="utf-8")
        self.assertIn(".sidebar .main-nav{display:none!important}", css)
        self.assertIn(".sidebar .mobile-module-jump{display:flex!important;", css)
        self.assertIn("max-width:900px", css)
    def test_original_link_remains(self):
        js = (ROOT/"docs"/"always_on_ui.js").read_text(encoding="utf-8")
        self.assertIn("sourceLink=link(e.url", js)
        self.assertIn("actions.append(sourceLink,readBtn,saveBtn)", js)
        self.assertIn("noopener noreferrer", js)
    def test_prompt_retains_nonremoval_requirement(self):
        prompt=(ROOT/"MASTER_PROMPT_CO_v2.2.md").read_text(encoding="utf-8")
        self.assertIn("Nienaruszalność funkcji", prompt)
        self.assertIn("UPRASZCZAJ DROGĘ DO FUNKCJI, NIE FUNKCJE", prompt)

if __name__ == "__main__":
    unittest.main()
