import json
import math

with open("index.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
docs = len(content)
parsed_docs = []
for doc in content:
    parsed_docs.append(json.loads(doc))

dfs = {}
for page in parsed_docs:
    for site in page:
        for term in page[site]:
            if term in dfs:
                dfs[term] += 1
            else:
                dfs[term] = 1

for entry in dfs:
    dfs[entry] = math.log10(docs / dfs[entry])

tidfs = {}

for doc in parsed_docs:
    tidf = {}
    for site_content in doc:
        for term in doc[site_content]:
            tidf[term] = (1+ math.log10(doc[site_content][term])) * dfs[term]
        tidfs[site_content] = tidf

with open('tf-idf.txt', 'a') as the_file:
    the_file.write(str(tidfs))