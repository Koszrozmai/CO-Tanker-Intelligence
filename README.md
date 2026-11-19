# CO Tanker Intelligence v1.8

Chief Officer / chemical and product tanker assistant, installation in Chrome and Android/Samsung.

## Website (after Pages is enabled)
https://koszrozmai.github.io/CO-Tanker-Intelligence/

**Chrome Windows:** open the website and use it in the browser. **Chrome on Samsung:** open URL, choose menu > Add to Home screen / Install app, then launch the icon.

## Scheduled public-source collector
Workflow: [Check sources and deploy](./.github/workflows/collect.yml). Runs on each push, manually and approximately every three hours (UTC). The collector retrieves **public index pages** from allow-listed source domains and saves `docs/data/intelligence.json` with timestamps, source health and new link discoveries. This is *not* a guarantee of always-on execution. Each retrieved item is a **link requiring primary-source review**, not legal validation or ship-specific operational advice. Unavailable sources are marked unavailable; the application must not imply that they were successfully checked.

For an updated live feed, Pages must be enabled in **Settings > Pages > Build and deployment > Source: GitHub Actions**, and the workflow must complete successfully. A public GitHub Pages website is **not owner-private**; do not enter private crew, cargo, company or vessel data there.

## Safety and backups
The browser saves personal study progress and notes locally. Export your JSON backup before changing browser/origin/device. Reimport on a new device as needed. Data does not automatically sync between devices.

The bundled training cards are general references. For operational decisions always check the vessel's approved SMS/QMS, cargo information, flag/class requirements, OEM revision and official original documents.
