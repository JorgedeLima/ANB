# Auckland New Ballet website

Live at https://www.aucklandnewballet.co.nz. Every push to `main` runs `.github/workflows/pages.yml`, which builds the site with `tools/build_site.py` and publishes it to GitHub Pages (about a minute; progress is under the repo's Actions tab).

**This repo is the source of truth.** Edit the files here and push to `main`. Don't replace `index.html` with a new Claude Design export, because that would overwrite every change made here since. Use Claude Design for new design ideas, then port the approved design into this repo by hand.

## Layout

| Path | What it is |
|---|---|
| `index.html` | The whole site. Each page is an `<sc-if value="{{ isHome }}">` (`isAbout`, `isArtists`, `isProgrammes`, …) block; the footer follows them. Page data (leadership, donors, nav, donation tiers) is in the `<script type="text/x-dc">` block near the bottom. |
| `static/img/` | Images used by the site, named after the slot or subject they fill. |
| `static/fonts/` | Cormorant Garamond and Instrument Sans (self-hosted). |
| `static/video/anb-hero.mp4` | Home page hero video. |
| `static/js/` | Claude Design runtime (`dc-runtime.js`), image slot component (`image-slot.js`) and React 18.3.1. Don't edit. |
| `CNAME` | Custom domain. Keep it, or the domain detaches from Pages. |
| `404.html` | Fallback for unknown addresses: hands them to the site, which opens the home page. |
| `tools/build_site.py` | Builds the published site: a copy of `index.html` at each page address with its own title, description and share tags, plus `sitemap.xml` and `robots.txt`. Edit page titles and descriptions here. |
| `.github/workflows/pages.yml` | Runs the build and publishes on every push to `main`. |
| `assets/`, `uploads/`, `video/` | Original source material from the client. Not published. |
| `docs/` | Site structure and the Claude Design handoff brief. |
| `archive/claude-design/` | The last Claude Design source and export notes, kept for reference. Not published. |

## Page addresses

Each page has its own address: `/`, `/about/`, `/artists/`, `/leadership/`, `/collaborators/`, `/programmes/`, `/donate/`, `/sponsors/`, `/contact/`. An artist's biography is `/artists/#artist-zoe` (the `id` on their section).

To add or rename a page, update `ROUTES` and `TITLES` in the script block of `index.html` and `PAGES` in `tools/build_site.py`. The build fails if `ROUTES` and `PAGES` don't match.

Asset paths start with `/static/` so they work from every address.

## Making changes

1. Edit `index.html` or add files under `static/`.
2. Preview locally: `python3 tools/build_site.py`, then `python3 -m http.server 8192 -d _site` and open http://localhost:8192 (any page address works there).
3. Commit and push to `main`. `_site/` is ignored by git.

Unpacked on 17 Oct 2026 from the Claude Design export committed as `Oct14_V1.1` (c44d81e), with no visual or content changes.
