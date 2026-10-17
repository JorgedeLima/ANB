# ANB website — deploy to GitHub Pages

Repo: JorgedeLima/ANB · branch: main · Pages source: main / (root)

## Instructions for Claude Code

1. Place `index.html` (this folder) at the repo root, replacing the existing `index.html`.
2. The file is self-contained (~26 MB, hero video embedded) — no other assets needed. Under GitHub's 100 MB limit; no Git LFS required.
3. Commit: `Update ANB site: tour details, home Folklore dates + artwork, Programmes hero artwork`
4. Push to `main`.
5. If Pages isn't enabled yet: `gh api -X POST repos/JorgedeLima/ANB/pages -f "source[branch]=main" -f "source[path]=/"`
6. Live at https://jorgedelima.github.io/ANB/ within ~1 minute.

## Changes in this export

- Programmes: Folklore key art (1170×504) as page hero, uncropped
- Programmes: "Upcoming performances" replaced with Tour details — Whanganui, Waiheke Island, Tauranga
- Home: Folklore dates updated to the tour (date-first rows); intro copy updated
- Home: Folklore 4:3 artwork beside the dates
- Earlier in this release: self-hosted hero video with independent Pause/Sound controls, Kulios carousel captions, all sponsor logos, Meaghan Rowe bio

## Known before launch

- Whanganui Eventfinda URL needed — Buy Tickets buttons still point to an in-page anchor
- Tauranga month assumed February — confirm
- Programmes page still names Holy Trinity Cathedral, Parnell; Summer Regional Tour note still lists Kerikeri
- Artist headshots and Francesca Fong photo still placeholders
- Content-gap notes visible unless hidden via the Tweaks toggle before export
