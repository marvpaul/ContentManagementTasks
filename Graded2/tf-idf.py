import json
import math

with open("index.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]
docs = len(content)
idfs = {}
for page in content:
    websiteTF = json.loads(page)
    for site in websiteTF:
        for tf in websiteTF[site]:
            if tf in idfs:
                idfs[tf] += 1
            else:
                idfs[tf] = 1

for entry in idfs:
    idfs[entry] = math.log10(docs / idfs[entry])

with open('tfids.txt', 'a') as the_file:
    the_file.write(str(idfs))