# ANB website — deploy to GitHub Pages

Repo: JorgedeLima/ANB · branch: main · Pages source: main / (root)

## Instructions for Claude Code

1. Place `index.html` (this folder) at the repo root, replacing any existing `index.html`.
2. The file is self-contained (~26 MB, hero video embedded) — no other assets needed. It is under GitHub's 100 MB file limit; no Git LFS required.
3. Commit: `Update ANB site: self-hosted hero video, sound/pause controls, Kulios captions`
4. Push to `main`.
5. If Pages isn't enabled yet: `gh api -X POST repos/JorgedeLima/ANB/pages -f "source[branch]=main" -f "source[path]=/"`
6. Live at https://jorgedelima.github.io/ANB/ within ~1 minute.

## Changes in this export

- Hero: YouTube embed replaced with self-hosted `ANB_hero_video_480.mp4` (muted autoplay, loops)
- Hero: Pause/Play and Sound on/off are independent; sound choice persists while paused
- Kulios carousel: Francesca Fong — viola, Peau Halapua — violin
- Reduced-motion users get the static poster instead of video

## Known before launch

- Ticket buttons still link to an in-page anchor — box office URL pending
- Artist headshots, Francesca Fong photo and M. D. Fotti logo still placeholders
- Content-gap notes visible unless hidden via the Tweaks toggle before export
