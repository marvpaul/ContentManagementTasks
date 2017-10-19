from urllib import request, parse

from htmldom import htmldom
import sqlite3
import Task1

def saveDescAndAltToDatabase(linkName, alt, con, cur):
    query = "insert into xkcd values ('" + linkName + "', '" +  alt + "')"
    cur.execute(query)
    con.commit()

def getAltAttrFromArticle(link):
    base = 'http://xkcd.com'
    linkCompl = parse.urljoin(base, link)
    f = request.urlopen(linkCompl)
    content = str(f.read(), 'utf-8')

    dom = htmldom.HtmlDom().createDom(content)
    return [dom.find('#comic').find('img').attr('title'), linkCompl]


def searchForQueryInDesc(query):
    with sqlite3.connect('xkcd_db.db') as con:
        cur = con.cursor()
        query = "SELECT url FROM xkcd WHERE instr(alt,'" + query + "')> 0 "
        cur.execute(query)

    urls = []
    for (url) in cur:
        urls.append(url[0])
    return urls


def downloadAndSaveArticles():
    #Get links
    links = Task1.getComicLinks()[0:10]

    #download site and select description in title tag
    descs = []
    for link in links:
        href = link.attr('href')
        descs.append(getAltAttrFromArticle(href))

    #Save queried data in database
    with sqlite3.connect('xkcd_db.db') as con:
        cur = con.cursor()
    cur.execute('drop table if exists xkcd')
    cur.execute('create table xkcd (url text, alt text)')
    for desc in descs:
        saveDescAndAltToDatabase(desc[1], desc[0], con, cur)


print(searchForQueryInDesc('not'))