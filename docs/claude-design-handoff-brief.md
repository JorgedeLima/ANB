# Auckland New Ballet, Claude Design Handoff Brief

Scope of this round: structure, copy, look and feel, and interactions, for approval as a proof of concept. Not a live-launch package, so ticketing/venue specifics don't need to be locked yet.

## How to actually hand this off

Try this first: if Claude Design lets you open a session inside this same "ANB Auckland New Ballet" project on claude.ai, do that rather than starting fresh elsewhere. Projects are shared across claude.ai surfaces, so a session opened inside it should already see this brief, `site-structure.md`, `ANB website_copy.pdf`, and `ANB Logo.jpg` without you re-uploading anything.

If Claude Design instead opens as a clean, unconnected session with no project context, hand it exactly four things: paste this brief's text as your opening message, and attach the other three files directly, the sitemap doc, the full copy PDF, and the logo. Don't paraphrase the copy into the new session by hand, the PDF is the source of truth and re-typing it invites drift.

## What's already decided

Five top-level sections (Home, Who We Are, What We Do, Support ANB, Get in Touch), a single combined "ANB Artists" roster page rather than individual dancer pages, ticket links that point out to wherever each performance is actually sold rather than a native checkout, and "Upcoming Programmes" built as a repeatable content block rather than static text. Full detail and the reasoning behind each is in `site-structure.md`, no need to restate it here, point Claude Design there.

## Brand identity, read from the logo you already have on file

The wordmark sets "ANB" in a classic serif display, wide letterspacing, near-black, with "Auckland New Ballet" beneath it in a smaller, more delicate serif in a deep indigo-plum ink, on a soft pale lavender-grey field. That's a restrained, editorial mark, closer to a gallery catalogue or a literary imprint than a typical performing-arts logo. It's worth naming as a real design decision point: it points the visual system toward serif display type and a muted, warm-neutral palette (lavender-greys, near-black, and probably one deeper accent, plum or a muted gold) rather than the high-contrast black-and-white or saturated color you'll see on some of your own references.

## Look and feel, from what your five references actually look like right now

NDT runs a full-width autoplay video hero, sans-serif type, dark photography-driven color, and a sticky nav with a prominent Tickets button, everything reads as contemporary and editorial rather than ornate. BalletX leans on a large hero image over a bold contemporary-dance headline, white space, dropdown navigation, and a visible Instagram feed and carousel of dancer profiles, closer to a lifestyle brand than an institution. Akram Khan Company is the most stripped-back of the five, video-forward, minimal chrome, almost no decorative color, it trusts the footage to carry the brand. Royal Ballet School and Opéra de Paris are the two closest cousins to ANB in mission, both use image carousels rather than a single hero, dark navigation with high contrast, and deep mega-menus, because they're managing far more content than ANB will ever need to.

The throughline across all five: sans-serif interface type, photography and video doing the emotional work rather than color or ornament, and a small number of insistent CTA buttons (Tickets, Donate, Book) that never get buried. Where ANB should diverge is exactly the point above, your own mark is serif and quietly classical where every one of these references is sans-serif and contemporary. That's not a contradiction to resolve, it's a legitimate point of difference, classical ballet company, not a contemporary dance company, and the logo already says so. Worth telling Claude Design explicitly: keep the sans-serif discipline for body copy and navigation (all five references agree on this for a reason, it's legible and gets out of the way), but let the serif carry headlines, page titles, and pull quotes, so the site doesn't accidentally read as one more contemporary-dance brand.

## Interaction and technical notes to carry forward

Motion.dev is specified for micro-interactions; `site-structure.md` already flags that this is a real Wix custom-code dependency, not a checkbox in the visual editor, worth Claude Design confirming feasibility for whatever specific interactions it proposes rather than promising something that can't ship on Wix. The homepage hero is video per the brief, needs a pause control and a static poster fallback from day one, not added later. All five references use a persistent, unmissable primary CTA, ANB's equivalent for this POC stage can be a placeholder "Buy Tickets" / "Donate" button pair, since the destination isn't locked yet, but the pattern should be designed in now.

## Content gaps Claude Design should design around, not wait on

None of the artist, leadership, or collaborator headshots exist yet, Grace Ella's bio is still a placeholder in the copy doc, the mailing list tool isn't chosen, and donor consent for public naming on the Sponsors page hasn't been confirmed. For a structure-and-feel approval round this is fine, use a consistent placeholder avatar treatment for every missing headshot rather than blocking on real photography, but it's worth saying out loud so nobody mistakes a placeholder for a finished page.

## Before you send this

Worth deciding now, not after you see the first mockups: what does "approved" actually mean for this round, specifically? Structure, copy tone, and look-and-feel direction are three different things to sign off on, and it's easy for a POC review to quietly collapse into "do I like this color" while the sitemap and copy tone go unexamined. And since this is ANB's brand, not just yours, worth getting at least one dancer or board member's eyes on it alongside your own before you call it approved, taste read from inside the company will catch things a design-trained eye won't.
