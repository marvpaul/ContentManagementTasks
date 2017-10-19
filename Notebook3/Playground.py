import pprint
from urllib import request, parse
from htmldom import htmldom

base = 'http://xkcd.com'
archive = parse.urljoin(base, 'archive')

#Load article
f = request.urlopen(archive)
content = str(f.read(), 'utf-8')

archive_html = htmldom.HtmlDom().createDom(content)
middleContainer = archive_html.find('#middleContainer')
anchors = middleContainer.find('a')
comic_a = anchors[0]
comic_url = parse.urljoin(base, comic_a.attr('href'))
print(comic_url)

#Some os tries
import os
print(os.name)
print(os.getcwd())
os.makedirs('xkcd', exist_ok=True)