import json
import unittest
from pathlib import Path
from collector import run, provenance, relevant_to_co, listing_label
from source_discovery import candidates_from_html
from test_collector import FakeSession, SRC

class ProvenanceTests(unittest.TestCase):
    def test_all_registry_sources_have_valid_type(self):
        rows=json.loads(Path(__file__).with_name('sources.json').read_text('utf-8'))
        self.assertEqual(len({r['id'] for r in rows}),len(rows))
        self.assertTrue(all(r['source_class'] in ('regulator','industry_body','editorial','social') for r in rows))
        self.assertTrue(all(r['url'].startswith('https://') and r['host'] for r in rows))

    def test_existing_official_entry_labeled(self):
        s={**SRC,'source_class':'regulator'}
        feed=run([s],{'entries':[],'sources':[]},session=FakeSession())
        self.assertEqual(feed['entries'][0]['source_class'],'regulator')
        self.assertIn('OFICJALNE',feed['entries'][0]['source_label'])
        self.assertIn('NOT verified',feed['entries'][0]['status_label'])

    def test_old_news_gets_relabelled(self):
        base=run([SRC],{'entries':[],'sources':[]},session=FakeSession())
        old=base['entries'][0];old.pop('source_label',None)
        src={**SRC,'source_class':'editorial'}
        newer=run([src],base,session=FakeSession())
        self.assertIn('NIEOFICJALNE',newer['entries'][0]['source_label'].upper())

    def test_trade_coverage_filter(self):
        source={'source_class':'editorial'}
        self.assertTrue(relevant_to_co('Tanker cargo mooring and port safety',source))
        self.assertFalse(relevant_to_co('Celebrity cooking tips and sports',source))

    def test_cdi_terminal_marketing_excluded(self):
        cdi={'id':'cdi','source_class':'industry_body'}
        self.assertFalse(relevant_to_co('CDI Welcomes Terminal Operator New Member', cdi))
        self.assertFalse(relevant_to_co('New CDI-T report for terminal Rotterdam', cdi))
        self.assertTrue(relevant_to_co('CDI Announces Alternative Energy & Power Supply Questionnaire', cdi))

    def test_discovery_does_not_autoapprove(self):
        source='https://safety4sea.com/'
        raw='<a href="https://marineexample.org/">Maritime training and tanker safety</a><a href="https://facebook.com/example">Facebook</a><a href="http://unsafe.example/">Maritime updates</a>'
        proposals=candidates_from_html(source,raw,{'safety4sea.com'})
        self.assertEqual(len(proposals),1)
        self.assertEqual(proposals[0]['approval'],'PENDING HUMAN REVIEW')
        self.assertEqual(proposals[0]['host'],'marineexample.org')

if __name__=='__main__':unittest.main()
