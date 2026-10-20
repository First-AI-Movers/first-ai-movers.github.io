#!/usr/bin/env python3
"""Validate the static Pages tree without network access or dependencies."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://first-ai-movers.github.io/'


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.links, self.ids, self.headings, self.jsonld = [], set(), [], []
        self.block = None
        self.feed(source)
        self.close()
        assert self.block is None, 'unclosed JSON-LD script'

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'duplicate id'
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.headings.append(int(tag[1]))
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.block = ''

    def handle_data(self, data):
        if self.block is not None:
            self.block += data

    def handle_endtag(self, tag):
        if tag == 'script' and self.block is not None:
            self.jsonld.append(json.loads(self.block))
            self.block = None


def local_target(url):
    parsed = urlsplit(url)
    assert parsed.scheme == 'https' and parsed.netloc == urlsplit(ORIGIN).netloc
    path = (ROOT / unquote(parsed.path).lstrip('/')).resolve()
    assert path.is_relative_to(ROOT), 'link escapes site root'
    if path.is_dir():
        path /= 'index.html'
    assert path.is_file(), f'missing internal target: {parsed.path}'
    return path, unquote(parsed.fragment)


def main():
    pages = {path: Page(path.read_text()) for path in ROOT.glob('*.html')}
    assert ROOT / 'index.html' in pages, 'missing homepage'
    count = 0
    for path, page in pages.items():
        assert page.headings.count(1) == 1, f'{path.name}: expected one h1'
        assert page.headings[0] == 1
        assert all(b <= a + 1 for a, b in zip(page.headings, page.headings[1:])), 'heading level skipped'
        for href in page.links:
            url = urljoin(ORIGIN + path.name, href)
            parsed = urlsplit(url)
            if parsed.netloc != urlsplit(ORIGIN).netloc or parsed.scheme != 'https':
                continue
            target, fragment = local_target(url)
            if fragment:
                assert target in pages and fragment in pages[target].ids, f'missing fragment: {href}'
            count += 1
    assert pages[ROOT / 'index.html'].jsonld, 'homepage has no JSON-LD'
    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    sitemap = ET.parse(ROOT / 'sitemap.xml').getroot()
    assert sitemap.tag == ns + 'urlset', 'invalid sitemap root'
    locations = [node.text for node in sitemap.findall(ns + 'url/' + ns + 'loc')]
    assert locations and len(set(locations)) == len(locations), 'empty or duplicate sitemap locations'
    for location in locations:
        target, fragment = local_target(location)
        assert target in pages and not fragment, 'sitemap must name an HTML page without fragment'
    assert 'Sitemap: ' + ORIGIN + 'sitemap.xml' in (ROOT / 'robots.txt').read_text()
    print(f'PASS: {len(pages)} HTML pages, {count} internal links, {len(locations)} sitemap URLs, JSON-LD and headings')


if __name__ == '__main__':
    main()
