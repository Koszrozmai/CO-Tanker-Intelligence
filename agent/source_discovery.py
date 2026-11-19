#!/usr/bin/env python3
"""Suggest new maritime publishers for human review; never enable them automatically.

Discovery reads only public HTTPS pages from the explicit, curated seed list.
No login, social scraping, arbitrary URL ingestion, or regulatory inference.
"""
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
import requests
from lxml import html

ROOT=Path(__file__).resolve().parents[1]
SEEDS=[
    "https://www.imo.org/en/mediacentre/pressbriefings/pages/default.aspx",
    "https://www.emsa.europa.eu/newsroom/latest-news.html",
    "https://www.marineinsight.com/",
    "https://safety4sea.com/",
    "https://gcaptain.com/",
    "https://insidemarine.com/",
]
DENY={
    "google.com","youtube.com","facebook.com","instagram.com","tiktok.com",
    "linkedin.com","x.com","twitter.com","pinterest.com","wordpress.org",
    "wikipedia.org","amazon.com","apple.com","microsoft.com","cloudflare.com",
    "github.com","whatsapp.com","reddit.com"
}
SIGNALS=re.compile(r"maritime|shipping|shipowner|tanker|naval|seafarer|marine|nautical|"
                   r"port.state|classification.society|flag.state|coast.guard|"
                   r"safety.at.sea|marpol|solas|imo|ocimf|vetting|marine.insight|"
                   r"shipping.news|marine.news",re.I)

def domain(host):
    host=(host or "").lower().removeprefix("www.")
    return host

def candidates_from_html(base,markup,registered):
    tree=html.fromstring(markup)
    found={}
    for a in tree.xpath('//a[@href]')[:1500]:
        href=a.get("href","")
        try:
            u=urlparse(href)
            if u.scheme!="https" or not u.hostname or u.username or u.password or u.port not in (None,443):
                continue
        except ValueError:
            continue
        host=domain(u.hostname)
        if host in registered or host in DENY or any(host.endswith("."+d) for d in DENY):
            continue
        if host==domain(urlparse(base).hostname) or host.endswith("."+domain(urlparse(base).hostname)):
            continue
        title=" ".join(a.itertext()).strip()[:150]
        if not SIGNALS.search(host+" "+title):
            continue
        found[host]={"host":host,"example_url":"https://"+host+"/",
                     "found_via":base,"link_context":re.sub(r"\\s+"," ",title),
                     "approval":"PENDING HUMAN REVIEW",
                     "publisher_type":"UNASSESSED",
                     "note":"Outbound link only. No credibility, identity or content verification performed."}
    return list(found.values())

def discover(seeds=SEEDS,fetch=None):
    fetch=fetch or requests.Session()
    registered={domain(x["host"]) for x in json.loads((ROOT/"agent/sources.json").read_text("utf-8"))}
    pending={}
    checks=[]
    for seed in seeds:
        try:
            r=fetch.get(seed,timeout=(5,12),allow_redirects=False,
                        headers={"User-Agent":"CO-Tanker-Intelligence/1.6 (public publisher discovery)"})
            if r.status_code!=200 or len(r.content)>900000:
                raise ValueError("HTTP "+str(r.status_code)+" or oversized response")
            for c in candidates_from_html(seed,r.text,registered):
                pending.setdefault(c["host"],c)
            checks.append({"seed":seed,"status":"ok"})
        except (requests.RequestException,ValueError) as ex:
            checks.append({"seed":seed,"status":"unavailable","error":str(ex)[:120]})
    return {"generated_at":datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "approval_policy":"All candidates remain inactive pending publisher identity, editorial quality, HTTPS and access review",
            "candidates":list(pending.values())[:80],"checks":checks}

def main():
    output=ROOT/"docs/data/source_candidates.json"
    fresh=discover()
    prior={}
    if output.exists():
        try:prior=json.loads(output.read_text("utf-8"))
        except (ValueError,OSError):pass
    # Keep unapproved candidates from recent scans. Existing sources are excluded.
    registered={domain(x["host"]) for x in json.loads((ROOT/"agent/sources.json").read_text("utf-8"))}
    seen={x["host"]:x for x in prior.get("candidates",[]) if
          isinstance(x,dict) and x.get("approval")=="PENDING HUMAN REVIEW" and x.get("host") not in registered}
    for x in fresh["candidates"]:seen[x["host"]]=x
    fresh["candidates"]=list(seen.values())[-80:]
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(fresh,ensure_ascii=False,indent=2)+"\n","utf-8")
    print("Discovery candidates:",len(fresh["candidates"]),
          "seed checks:",len(fresh["checks"]),"pending approval; zero auto-approved")

if __name__=="__main__":main()
