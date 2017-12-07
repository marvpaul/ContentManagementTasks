from os import listdir
from os.path import join, isfile
import numpy as np
from htmldom import htmldom


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

links = analyzeDocs()
link_matrix_with_teleportation = apply_teleportation_rate(links)


gamma = 0.04
