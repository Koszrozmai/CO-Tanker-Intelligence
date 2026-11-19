# CO Tanker Intelligence — source credibility and discovery policy (19 November 2026)

## Provenance shown to the officer

- **OFICJALNE — organ / administracja**: public administrations and official maritime authorities (IMO, Cyprus flag, Paris MoU, EMSA, MCA). Official publisher status does NOT mean that a headline has statutory effect.
- **ORGANIZACJA BRANŻOWA — nie stanowi prawa**: OCIMF, CDI-M, BIMCO, INTERTANKO. Relevant programmes and industry guidance may have independent contractual or vetting significance.
- **MEDIA BRANŻOWE — nieoficjalne**: Inside Marine, Marine Insight, gCaptain, SAFETY4SEA, The Maritime Executive. These are editorial/trade perspectives, not authorities.
- **SOCIAL / YOUTUBE — nieoficjalne**: publisher-linked public video channels. Identify author and original video link. No personal Facebook account scraping, paywall bypass or implied endorsement.

All source types have the same **document status** distinction: RSS/listing headline, original reviewed, or proposed interpretation. The scheduled collector produces **listing** metadata, never a verified legal requirement. Links lead to the publisher; technical and legal application is assessed against primary instruments, flag, SMS/QMS, P&A and current operational context.

## Continuous discovery

Every normal three-hour scheduled collector run also invokes `agent/source_discovery.py`. It visits a small, fixed set of known public maritime publisher and authority pages and extracts relevant outbound domains. Suggestions appear in `docs/data/source_candidates.json` with **PENDING HUMAN REVIEW** status, but are **never automatically crawled or activated**. Existing registered publishers remain active irrespective of new suggestions.

Review a candidate for:
1. Identifiable publisher, editorial ownership, corrections policy and original reporting;
2. Relevant Chief Officer / chemical and product tanker content, not volume of social likes;
3. Factual evidence, dates, source attribution, conflicts and technical credibility;
4. Public HTTPS access and permitted official RSS/API or stable public page; no 403/429 bypass;
5. Disinformation, affiliate influence, scraped reposts, fabricated regulatory dates, content farms.

Approved publishers must be manually added to `agent/sources.json` with `source_class`, `channel`, `editorial_review`, `host`, `url`, and a tested parser. Rejected candidates can be removed or explicitly logged as declined during review.

## Current limits

- A YouTube channel may be monitored only through a working public feed. A Facebook page with no lawful public RSS/API feed is not continuously scraped.
- GitHub Actions attempts runs on its schedule but does not guarantee minute-accurate coverage; blocked sources remain visible as failed/deferred.
- The publisher registry is curated; headlines, syndication and individual claims have **not** been individually fact-checked.
- The source finder explores outbound links from selected seed pages, **not** the entire web. It does not automatically certify or onboard discoveries.
- Public GitHub contains no confidential onboard notes, crew documents, vessel checklists or training progress.
