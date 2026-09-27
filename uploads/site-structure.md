# Auckland New Ballet, Website Structure v1

Prepared for handoff to Claude Design. Hosting is Wix, source of truth is GitHub. Built from the project brief, `ANB website_copy.pdf`, and the four structural decisions we locked in on 15 September 2026 (recorded below).

## 1. Sitemap

```
Home                                          /

Who We Are                                    /who-we-are
  About Us                                    /who-we-are/about
  ANB Artists                                 /who-we-are/artists
  ANB 2027 Leadership                         /who-we-are/leadership
  Artistic Collaborators                      /who-we-are/collaborators

What We Do                                    /what-we-do
  Upcoming Programmes                         /what-we-do/upcoming-programmes

Support ANB                                   /support
  Ways to Donate                              /support/donate
  Current Sponsors                            /support/sponsors

Get in Touch                                  /contact
```

Global, not standalone pages: header nav, footer (social links, mailing list signup, logo, copyright), a persistent "Buy Tickets" CTA in the header, and a secondary "Donate" CTA in the footer.

## 2. Page by page

| Page | URL | Purpose | Key content (from your copy doc) | Notes / gaps |
|---|---|---|---|---|
| Home | `/` | First impression, route people to a ticket or a donation | Full-bleed video hero, one-line mission statement, teaser for the current season with dates, sponsor logo strip, Instagram teaser, mailing list signup | Needs a static poster-frame fallback for mobile and for anyone with reduced-motion set. No hero copy exists yet, this is new writing. |
| About Us | `/who-we-are/about` | Origin story, mission, values | Founding story (seven freelance dancers), mission statement, the six founding principles, Auckland/Tāmaki Makaurau framing | Copy is complete and strong as-is. |
| ANB Artists | `/who-we-are/artists` | Introduce the company as people | Bios for Madison Fotti-Knowles, Amelia Chandulal-Mackay, Zoe White, Isabella Guyan, Kimberley Mear, Louis Ramsay, Katrina Casey, Grace Ella | One combined roster page per your decision, with an anchor link per artist. Grace Ella's bio is still a placeholder ("BIO HERE"). Profile photos for all eight are needed and don't exist in the project yet. |
| ANB 2027 Leadership | `/who-we-are/leadership` | Show who runs the company | Creative Director, Producer, Support Producer, Rehearsal Director, Social Media Manager, each mapped to a name already listed on the Artists page | Worth flagging even though it wasn't one of the four questions: four of these five names are dancers already bio'd on the Artists page. Consider this page as a short role table that anchor-links back to each person's existing bio, rather than a second set of write-ups, so you're not maintaining the same person's story twice. |
| Artistic Collaborators | `/who-we-are/collaborators` | Credit non-dancer creative contributors | Zara Ridley (Technician in Residence), Kulios Ensemble (Musicians in Residence) | Thin content today, two entries. Fine as a page, but don't over-invest design effort here relative to Artists. |
| Upcoming Programmes | `/what-we-do/upcoming-programmes` | Sell the current season | Folklore (2 acts: Tales of the Past, Songs of Tomorrow), venue and dates, Quiet Matinee description, post-show Q&A, Summer Regional Tour teaser (Waiheke, Whanganui, Tauranga, Kerikeri) | Per your decision, each listed performance gets its own "Buy Tickets" link out rather than a native checkout. See Section 5 on why this should be a repeatable content block, not static text. |
| Ways to Donate | `/support/donate` | Convert visitors into pointe shoe fund donors and sponsors | Pointe Shoe Fund story, five giving tiers ($40 / $90 / $135 / $675 / $2,000), "Sponsor us" prompt for businesses | See Section 6 on tier ordering, it isn't a neutral design choice. |
| Current Sponsors | `/support/sponsors` | Recognise funders publicly | Logo-worthy sponsors (M. D. Fotti, Family Office Advisory, Pure Dance, Erin Bowerman Strength and Conditioning, Wellesley Studios, Auckland Council) plus a named list of eight individual 2026 donors | Publishing named individuals (Hamish Mackay, Doug and Marianne Cooper, etc.) needs each person's sign-off on public listing, confirm this is already in hand before it goes live. |
| Contact Us | `/contact` | Direct enquiries, capture emails | `aucklandnewballet@gmail.com`, Instagram (@aucklandnewballet), Facebook, mailing list signup | The copy doc references a mailing list link that doesn't resolve to a named tool yet (Mailchimp, Wix's own contacts app, etc.), needs deciding before this page can be built for real. |

## 3. Decisions locked this session

Dedicated "Support ANB" nav item, matching your copy doc rather than the original brief's placement of Sponsors under "What We Do." Ticketing is link-out per performance to whichever provider actually holds the box office for that date and venue (Holy Trinity Cathedral events are commonly sold through iTICKET, worth confirming that's what Folklore is using). Artist bios live on one combined roster page rather than individual profile pages. And this document is saved both as a project doc here and committed into your ANB GitHub repo at `docs/site-structure.md`.

## 4. What I assumed, and what's still open

I assumed the hero video doesn't exist yet and is a production task, not a licensing or stock-footage task, given the brand is about your own dancers. I assumed "pay via the website" in the brief refers to ticket purchase, not a separate general payment page, since nothing else in the copy needs a standalone checkout beyond tickets and donations. I assumed the mailing list signup is a footer-level component rather than its own page, since the copy doc treats it as a single line, not a page.

What's genuinely still open, and worth resolving before this goes to Claude Design: whether Grace Ella's bio and headshot will be ready before the design phase starts, since a placeholder in a design file tends to quietly become the launch copy if nobody circles back to it. Whether all eight donor names in the copy doc have actually consented to public listing, separate from being thanked privately. Which tool runs the mailing list, because that decides whether the signup is a simple Wix form or needs a third-party embed with its own accessibility and Motion.dev implications. And whether "buy tickets" for the regional tour dates will even be live by the time this launches, since the copy doc says those dates aren't announced yet.

## 5. Technical notes for the design and build phase

Wix Studio doesn't give you a true two-way GitHub sync for the visual site the way a code-first stack would. If GitHub is the source of truth, the realistic split is: this structure doc, written copy, and any Velo backend code live in GitHub, while the visual layout itself lives in Wix Studio's own version history. Worth agreeing now who owns edits on which side, so the two don't quietly drift apart six months in.

Motion.dev is a JavaScript animation library built for code-first sites. Wix Studio can run it through custom code embeds or Velo, but that's a real technical dependency, not a checkbox in the visual editor, confirm with whoever builds this that embedding it is feasible before it's promised in the design.

Treat "Upcoming Programmes" as a repeatable content item (a Wix CMS collection: title, act structure, venue, date, ticket link, sold-out flag) rather than a static page. Folklore's own listed dates, September 18th and 19th, are days away from today. A static page means someone hand-edits HTML every time a season changes or a show sells out; a collection means Jorge or whoever's running the site updates a row.

On accessibility: an autoplaying hero video needs a pause control, a caption track if there's spoken content, and a `prefers-reduced-motion` fallback to a static image, this isn't optional under WCAG 2.1 AA and it's cheaper to build in from the start than retrofit. Every artist photo needs real alt text (name and role, not "photo of dancer"). On SEO: each page needs its own title and meta description, the Upcoming Programmes page is a strong candidate for Event structured data (helps it surface in Google's event results), and the combined-roster decision on Artists means that page carries more on-page SEO weight than a split would, so its heading structure matters more. On mobile: a full-bleed video hero is real data weight on a phone connection, serve a compressed mobile variant or a poster image by default rather than the same file across breakpoints.

## 6. A behavioural note on the donation tiers

The five giving amounts, $40, $90, $135, $675, $2,000, aren't a neutral list, they're an anchoring ladder. Showing the $2,000 "outfit the whole company" tier first (or at least prominently) tends to make the $135 pointe shoe tier read as modest by comparison, which is the direction that usually raises average gift size. If the tiers get rendered in strict ascending price order with equal visual weight, you lose that effect by default. Worth deciding deliberately with Claude Design rather than letting the layout decide it for you, and worth A/B testing tier order once the page has real traffic, not just guessing once and moving on.

## 7. Before this goes to Claude Design

Close out, or at minimum flag as known gaps in the handoff: Grace Ella's bio and a headshot for all eight company members plus the two collaborators, sponsor logos in a usable format, confirmed donor consent for public naming, a decided mailing list tool, and a confirmed ticketing link for the September 18 to 19 Folklore shows specifically, since that's the one date-sensitive piece of content in the entire structure.

## 8. One thing worth sitting with before you brief a designer

This structure treats all five sections as roughly equal weight, which is the standard shape for an arts company site. But right now, today, you have exactly one business event that matters commercially: two performances happening in three days. The path from your homepage to a ticket for that show is Home, then What We Do, then Upcoming Programmes, three clicks and a scroll. Everything else on this sitemap, Leadership, Collaborators, the donor honour roll, matters for credibility and long-term fundraising, but none of it sells a seat this week.

Is this structure meant to be the permanent shape of the site, or is it actually v2, and what you need in the next 72 hours is a single, ugly, fast landing page that does nothing but sell out Folklore? Those are two different projects with two different timelines, and it's worth being honest with yourself about which one you're actually asking Claude Design for.
