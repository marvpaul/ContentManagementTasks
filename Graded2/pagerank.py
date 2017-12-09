from os import listdir
from os.path import join, isfile
import numpy as np
from htmldom import htmldom
from copy import deepcopy


def analyzeDocs():
    '''Analyze the given docs and return a link matrix'''
    files = [f for f in listdir("tutorial/") if isfile(join("tutorial/", f))]
    scraped_files = []
    for file in files:
        if "html" in file:
            scraped_files.append(file)
    scraped_files = sorted(scraped_files)

    link_matrix = np.zeros(shape=(len(scraped_files), len(scraped_files)))
    for file in range(len(scraped_files)):
        f = open("tutorial/" + scraped_files[file], 'r+')
        file_content = ''.join(f.readlines())
        archive_html = htmldom.HtmlDom().createDom(file_content)
        links = archive_html.find('a')
        for link in links:
            link_matrix[file, scraped_files.index(link.attr('href'))] += 1
    return link_matrix

def apply_teleportation_rate(link_matrix):
    t = 0.05
    d = 1 - t
    for row in range(len(link_matrix)):
        if sum(link_matrix[row]) != 0:
            active_links = list(link_matrix[row]).count(1)
            rate_without_teleportation = 0
            if active_links != 0:
                rate_without_teleportation = 1 / active_links

            for link in range(len(link_matrix[row])):
                if link_matrix[row][link] == 0:
                    link_matrix[row][link] = t / len(link_matrix[row])
                else:
                    link_matrix[row][link] = rate_without_teleportation * d + t / len(link_matrix[row])
        else:
            link_matrix[row] = np.ones(len(link_matrix)) * (1/len(link_matrix))
    return link_matrix

def get_sites_with_link_to_site(site, link_matrix):
    sites_with_link_to_site = []
    for scanned_site in range(len(link_matrix)):
        if link_matrix[scanned_site][site] != 0:
            sites_with_link_to_site.append(scanned_site)
    return sites_with_link_to_site

def get_page_ranks(actual_pageranks, link_matrix, t):
    '''
    Calculate the page rank after one iteration
    :param actual_pageranks: the given page ranks
    :param link_matrix: the link matrix
    :return: the new page ranks
    '''
    d = 1 - t
    new_ranks = []
    for page_rank in range(len(actual_pageranks)):
        sites_with_link_to_actual_sites = get_sites_with_link_to_site(page_rank, link_matrix)
        sum1 = 0
        for site in sites_with_link_to_actual_sites:
            sum1 += actual_pageranks[site] / sum(link_matrix[site])


        sites_with_null_links = []
        for site in range(len(link_matrix)):
            if sum(link_matrix[site]) == 0:
                sites_with_null_links.append(site)

        sum2 = 0
        for site in sites_with_null_links:
            sum2 += actual_pageranks[site] / len(actual_pageranks)

        new_ranks.append(d * (sum1 + sum2) + t / len(actual_pageranks))

    return new_ranks

links = analyzeDocs()
link_matrix_with_teleportation = apply_teleportation_rate(deepcopy(links))

gamma = 0.04
pagerankgs = 1 / (len(link_matrix_with_teleportation) * np.ones(len(link_matrix_with_teleportation)))
new_ranks = get_page_ranks(pagerankgs, links, 0.05)
act_gamma = 0
for rank in range(len(pagerankgs)):
    act_gamma += abs(pagerankgs[rank] - new_ranks[rank])

print(links)

while act_gamma > gamma:
    print("ranks applied!")
    pagerankgs = new_ranks
    new_ranks = get_page_ranks(pagerankgs, links, 0.05)
    act_gamma = 0
    for rank in range(len(pagerankgs)):
        act_gamma += abs(pagerankgs[rank] - new_ranks[rank])

print(pagerankgs)
#TODO: These values shouldn't be the right values, because f.e. pg 1 has 3 backlinks, 7 has only 1 backlink
#Perhaps there is a failure?