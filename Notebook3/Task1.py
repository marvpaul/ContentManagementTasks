
from urllib import request, parse
import os
from htmldom import htmldom

#Just download the 10 most recent comics from xkcd

#Analyze the start page to get comic links
def getComicLinks():
    base = 'http://xkcd.com'
    archive = parse.urljoin(base, 'archive')

    #Load article
    f = request.urlopen(archive)
    content = str(f.read(), 'utf-8')

    archive_html = htmldom.HtmlDom().createDom(content)
    middleContainer = archive_html.find('#middleContainer')
    return middleContainer.find('a')

'''Analye and extract the comic (image) 
from a given comic link and save it under a certain name '''
def saveImageFromArticle(link):
    base = 'http://xkcd.com'
    f = request.urlopen(parse.urljoin(base, link))
    content = str(f.read(), 'utf-8')

    dom = htmldom.HtmlDom().createDom(content)

    extractedSrcPath = dom.find('#comic').find('img').attr('src')
    name = str(extractedSrcPath).split('/')
    name = name[len(name)-1].split('.')[0].replace('_', ' ')
    imageLink = parse.urljoin(base, extractedSrcPath)


    dir = 'xkcd'
    os.makedirs(dir, exist_ok=True)
    with open((dir + '/' + name + '.png'), 'wb') as f:
        f.write(request.urlopen(imageLink).read())

def downloadSeveralImages():
    comicLinks = getComicLinks()[0:10]
    for link in comicLinks:
        saveImageFromArticle(link.attr('href'))


