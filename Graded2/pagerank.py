from os import listdir
from os.path import join, isfile
import numpy as np
from htmldom import htmldom


def analyzeDocs():
    '''Analyze the given docs and return a link matrix'''
    files = [f for f in listdir("crawler/") if isfile(join("crawler/", f))]
    doc_and_links = {}
    scraped_files = []

    #Get the files to analyze
    for file in files:
        if "html" in file:
            scraped_files.append(file)
            doc_and_links[file] = []

    #Analyze and parse the links from each site to another
    for document in doc_and_links:
        f = open("crawler/" + document, 'r+')
        file_content = ''.join(f.readlines())
        archive_html = htmldom.HtmlDom().createDom(file_content)
        links = archive_html.find('a')
        for link in links:
            doc_and_links[document].append(link.attr('href'))
    return doc_and_links

def get_sites_with_link_to_site(site, links):
    '''
    This method return all sites which include a link to site site
    :param site: the site we are searching for in the links of any other site
    :param links: all sites and links as dic
    :return: all sites which include a link to site site
    '''
    sites_with_link_to_site = []
    for document in links:
        if site in links[document]:
            sites_with_link_to_site.append(document)
    return sites_with_link_to_site

def get_page_ranks(actual_pageranks, links, t):
    '''
    Calculate the page rank after one iteration
    :param actual_pageranks: the given page ranks
    :param link_matrix: the link matrix
    :return: the new page ranks
    '''
    d = 1 - t
    new_ranks = {}
    for page_rank in pageranks:
        #Calculate sum 1 for pagerank
        sites_with_link_to_actual_sites = get_sites_with_link_to_site(page_rank, links)
        sum1 = sum([actual_pageranks[site] / len(links[site]) for site in sites_with_link_to_actual_sites])

        #Get all sites which has 0 links to other sites
        sites_with_null_links = []
        for site in links:
            if len(links[site]) == 0:
                sites_with_null_links.append(site)

        sum2 = sum([actual_pageranks[site] / len(actual_pageranks) for site in sites_with_null_links])

        #Apply new page rank
        new_ranks[page_rank] = (d * (sum1 + sum2) + t / len(actual_pageranks))

    return new_ranks

links = analyzeDocs()
print("Links from each site to each other site:")
print(links)

#Make some initial assigments
gamma = 0.04
initial_page_rank = 1 / (len(links))
pageranks = {}
for doc in links:
    pageranks[doc] = initial_page_rank
new_ranks = pageranks
act_gamma = 0

#Calculate a new page rank as long as the actual gamma is smaller than the given gamma
first_pass = True
while new_ranks != pageranks or first_pass:
    first_pass = False

    new_ranks = get_page_ranks(pageranks, links, 0.05)
    act_gamma = 0
    for rank in pageranks:
        act_gamma += abs(pageranks[rank] - new_ranks[rank])

    if act_gamma > gamma:
        pageranks = new_ranks

#Hopefully determined the correct page ranks
print("Page ranks:")
print(pageranks)

#Save the ranks
open('rank.txt', 'w').close()
with open('rank.txt', 'a') as the_file:
    the_file.write(str(pageranks))