# Auckland New Ballet website

Live at https://www.aucklandnewballet.co.nz (GitHub Pages, `main` branch, repo root).

**This repo is the source of truth.** Edit the files here and push to `main`; the site updates in about a minute. Don't replace `index.html` with a new Claude Design export, because that would overwrite every change made here since. Use Claude Design for new design ideas, then port the approved design into this repo by hand.

## Layout

| Path | What it is |
|---|---|
| `index.html` | The whole site. Each page is an `<sc-if value="{{ isHome }}">` (`isAbout`, `isArtists`, `isProgrammes`, …) block; the footer follows them. Page data (leadership, donors, nav, donation tiers) is in the `<script type="text/x-dc">` block near the bottom. |
| `static/img/` | Images used by the site, named after the slot or subject they fill. |
| `static/fonts/` | Cormorant Garamond and Instrument Sans (self-hosted). |
| `static/video/anb-hero.mp4` | Home page hero video. |
| `static/js/` | Claude Design runtime (`dc-runtime.js`), image slot component (`image-slot.js`) and React 18.3.1. Don't edit. |
| `CNAME` | Custom domain. Keep it, or the domain detaches from Pages. |
| `assets/`, `uploads/`, `video/` | Original source material from the client. Not used by the site. |
| `docs/` | Site structure and the Claude Design handoff brief. |
| `archive/claude-design/` | The last Claude Design source and export notes, kept for reference. |

## Making changes

1. Edit `index.html` or add files under `static/`.
2. Preview locally: `python3 -m http.server 8191` in this folder, then open http://localhost:8191.
3. Commit and push to `main`.

Unpacked on 17 Oct 2026 from the Claude Design export committed as `Oct14_V1.1` (c44d81e), with no visual or content changes.
