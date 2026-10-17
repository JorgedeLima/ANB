"""Build the published site into an output folder (default: _site).

GitHub Pages can only serve real files, so each page address (/artists/, /programmes/ ...)
gets its own copy of index.html with that page's title, description and share tags.
Search engines then see a normal page at every address. The site's own script still
handles moving between pages in the browser.

Run locally:  python3 tools/build_site.py _site  then  python3 -m http.server 8191 -d _site
The GitHub Actions workflow in .github/workflows/pages.yml runs this on every push to main.
"""
import html
import os
import re
import shutil
import sys
from datetime import date

SITE = 'https://www.aucklandnewballet.co.nz'
SHARE_IMAGE = '/static/img/og-folklore.jpg'

# path, title, description. Keep the paths in step with ROUTES in index.html.
PAGES = {
    'home': ('/', 'Auckland New Ballet',
             'Auckland New Ballet is Tāmaki Makaurau’s newest and only collective of professional ballet artists. '
             'Ballet as you’ve never experienced it: up-close, immersive, intimate.'),
    'about': ('/about/', 'About Us',
              'Auckland New Ballet began as seven freelance ballet dancers with a shared passion for connecting '
              'audiences with ballet, and a home for classical ballet in Auckland.'),
    'artists': ('/artists/', 'ANB Artists',
                'Seven professional ballet artists, trained across Moscow, London, Melbourne, New York and Aotearoa, '
                'who chose to build a home for classical ballet in Tāmaki Makaurau.'),
    'leadership': ('/leadership/', 'ANB 2027 Leadership',
                   'The Auckland New Ballet 2027 leadership team: Madison Fotti-Knowles, Zoe White, Isabella Guyan, '
                   'Meaghan Rowe and Amelia Chandulal-Mackay.'),
    'collaborators': ('/collaborators/', 'Artistic Collaborators',
                      'The people beyond the stage who shape how Auckland New Ballet’s work looks and sounds, '
                      'including Zara Ridley, the Kulios Ensemble and Gracie Lewis.'),
    'programmes': ('/programmes/', 'Folklore: Upcoming Programmes',
                   'Folklore, a ballet in two acts by Auckland New Ballet, touring Whanganui, Waiheke Island and '
                   'Tauranga this summer, with Quiet Matinees and evening performances.'),
    'donate': ('/donate/', 'Ways to Donate',
               'Support Auckland New Ballet. Our freelance dancers cover the cost of their own pointe shoes, and '
               'every donation, large or small, makes a world of difference.'),
    'sponsors': ('/sponsors/', 'Current Sponsors',
                 'Auckland New Ballet exists because of the people and organisations who backed a company that did '
                 'not exist yet. Meet our current sponsors and supporters.'),
    'contact': ('/contact/', 'Get in Touch',
                'Contact Auckland New Ballet and join the mailing list for season announcements, regional tour '
                'dates and ticket releases.'),
}

# What gets published. Source material (assets/, uploads/, video/, archive/, docs/) stays private.
COPY = ['static', 'CNAME', '404.html', 'favicon.ico']


def check_routes(src):
    """Fail the build if index.html's ROUTES and PAGES above have drifted apart."""
    m = re.search(r'static ROUTES = \{(.*?)\};', src)
    routes = dict(re.findall(r"(\w+): '([^']*)'", m.group(1)))
    mine = {k: v[0] for k, v in PAGES.items()}
    if routes != mine:
        sys.exit('ROUTES in index.html and PAGES in tools/build_site.py differ:\n  %s\n  %s' % (routes, mine))


def head_tags(path, title, desc):
    full = title if title == 'Auckland New Ballet' else title + ' | Auckland New Ballet'
    e = lambda x: html.escape(x, quote=True)
    return '\n'.join([
        '<title>%s</title>' % e(full),
        '<meta name="description" content="%s">' % e(desc),
        '<link rel="canonical" href="%s%s">' % (SITE, path),
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Auckland New Ballet">',
        '<meta property="og:title" content="%s">' % e(full),
        '<meta property="og:description" content="%s">' % e(desc),
        '<meta property="og:url" content="%s%s">' % (SITE, path),
        '<meta property="og:image" content="%s%s">' % (SITE, SHARE_IMAGE),
        '<meta name="twitter:card" content="summary_large_image">',
    ])


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(root, '_site'))
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)

    for name in COPY:
        src = os.path.join(root, name)
        (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, os.path.join(out, name))

    page = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
    check_routes(page)
    placeholder = '<title>Auckland New Ballet</title>'
    assert page.count(placeholder) == 1, 'index.html must contain exactly one ' + placeholder

    for key, (path, title, desc) in PAGES.items():
        dest = os.path.join(out, path.strip('/'), 'index.html')
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(page.replace(placeholder, head_tags(path, title, desc)))

    today = date.today().isoformat()
    with open(os.path.join(out, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for path, _, _ in PAGES.values():
            f.write('  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n' % (SITE, path, today))
        f.write('</urlset>\n')
    with open(os.path.join(out, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write('User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % SITE)

    print('Built %d pages into %s' % (len(PAGES), out))


if __name__ == '__main__':
    main()
