import math
import json

def search(query):
    #Read the term frequencies
    with open("index.txt") as f:
        content = f.readlines()

    content = [x.strip() for x in content]

    #Add the search query to tf dic
    search_query_words = query.split(" ")
    query_dic = {}
    for word in search_query_words:
        query_dic[word] = 1
    content.append("{\"search_query\":" + str(query_dic).replace("\'", "\"") + "}")

    #Parse from JSON to dics
    docs = len(content)
    parsed_docs = []
    for doc in content:
        parsed_docs.append(json.loads(doc))

    #Determine document frequencies for terms
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

    #Determine the tf-idf weights for all terms
    tidfs = {}
    for doc in parsed_docs:
        tidf = {}
        for site_content in doc:
            for term in doc[site_content]:
                tidf[term] = (1+ math.log10(doc[site_content][term])) * dfs[term]
            tidfs[site_content] = tidf

    #Get length of each tf-idf document vector
    doc_vec_length = {}
    for doc in tidfs:
        doc_vec_length[doc] = 0
        for value in tidfs[doc]:
            doc_vec_length[doc] += math.pow(tidfs[doc][value], 2)
        doc_vec_length[doc] = math.sqrt(doc_vec_length[doc])

    #Normalize the doc_vecs
    normalized_vecs = tidfs
    for doc in normalized_vecs:
        for value in normalized_vecs[doc]:
            normalized_vecs[doc][value] = normalized_vecs[doc][value] / doc_vec_length[doc]

    #Search in each document for search_query queries
    search_query = tidfs.pop("search_query")
    match = {}
    for doc in normalized_vecs:
        match[doc] = 0
        for value in search_query:
            if value in normalized_vecs[doc]:
                match[doc] += search_query[value] * normalized_vecs[doc][value]
    return match

#Lets do a search for the given queries and save results in tfidf_search
search_queries = ["tokens", "index", "classification", "tokens classification"]
result = ""
for query in search_queries:
    result += "{\"" + query + "\":" + str(search(query)) + "}\n"

print("Results:")
print(result)

#Save the results
open('tfidf_search.txt', 'w').close()
with open('tfidf_search.txt', 'a') as the_file:
    the_file.write(result)

