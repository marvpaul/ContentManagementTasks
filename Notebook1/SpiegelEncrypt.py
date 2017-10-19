from urllib import request
from htmldom import htmldom

def encrypt(string, shift):
    "Encrypt with caesar cipher"
    encryptedText = ""
    for char in list(string):
        encryptedText += chr((ord(char) + shift))
    return encryptedText

def encryptArticel(link):
    "Encrypt a given spiegel online article"

    #Load article
    f = request.urlopen(url)
    content = str(f.read(), 'utf-8')

    #Create dom and process selection
    dom = htmldom.HtmlDom().createDom(content)
    cryptedText = dom.find("p.obfuscated")

    encryptedArticle = ""
    for text in cryptedText:
        encryptedArticle += (encrypt(text.text(), -1) + "\n")
    return encryptedArticle

url = 'http://www.spiegel.de/spiegel/lidl-gruender-dieter-schwarz-der-koenig-von-heilbronn-a-1143420.html'
articleText = encryptArticel(url)

file = open("article", 'w')
file.write(articleText)







