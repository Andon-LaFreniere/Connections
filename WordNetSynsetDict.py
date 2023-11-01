#import Wordnet and the Natural Language Toolkit
from nltk.corpus import wordnet 
# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/
import sys
from SPARQLWrapper import SPARQLWrapper, JSON


print("Enter words all lowercase with a single space in between (ex: fun tool love)")
inp = input("Enter the 16 words you want to compare: ")
inps = inp.split(' ')


endpoint_url = "https://query.wikidata.org/sparql"
listS = []
for i in inps:
    sublist = []
    query = f"""
    SELECT  ?classLabel 
    WHERE 
    {{
        ?item rdfs:label "{i}"@en.
        ?item wdt:P279* ?class.
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
    }}
    """

    def get_results(endpoint_url, query):
        user_agent = "WDQS-example Python/{}.{}".format(sys.version_info[0], sys.version_info[1])
        # TODO adjust user agent; see https://w.wiki/CX6
        sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        return sparql.query().convert()

    results = get_results(endpoint_url, query)

    for result in results["results"]["bindings"]:
        for key, value in result.items():
            sublist.append(value['value'])
    listS.append(sublist)
def findSynonyms():
    dict = {}
    for h in inps:  #loop through each word in our input, finding the synonyms and adding them to a list. Add that list to a dictionary with the key being the word itself
        synonyms = [] 
        for syn in wordnet.synsets(h):
            for i in syn.lemmas():
                synonyms.append(i.name())
                dict.update({h:synonyms})

    return dict

def findHyper():
    hyperDict = {}
    for word in inps:
        My_sysn = wordnet.synsets(word)[0]
        hyperDict.update({word : My_sysn.hypernyms()})

    return hyperDict

def findHypo():
    hypoDict = {}
    for word in inps:
        My_sysn = wordnet.synsets(word)[0]
        hypoDict.update({word : My_sysn.hyponyms()})
    
    return hypoDict

dic3 = findHypo()
dic2 = findHyper()
dic = findSynonyms()
def percent():
    list = []
    for key in dic:
        list.append(dic[key])
    n = len(list)
    h = 1
    synList = []
    for i in range(1, n):
            for f in range(h, n):
                try:
                    common_elements = set(list[i-1]).intersection(set(list[f]))
                    num_common_elements = len(common_elements)
                    
                    # Find the total number of unique elements in both lists
                    total_elements = set(list[i-1]).union(set(list[f]))
                    num_total_elements = len(total_elements)
                    
                    # Calculate the percentage similarity
                    percentage_similarity = (num_common_elements / num_total_elements) * 100
                    
                    # Print the result
                    synList.append(format(percentage_similarity))
                except ZeroDivisionError:
                     synList.append(0.00)
            h=h+1
    print(synList)
    ################
    list2 = []
    for key2 in dic2:
        list2.append(dic2[key2])
    w = len(list2)
    r = 1
    hypList = []
    for i in range(1, w):
            for f in range(r, w):
                try:
                    common_elements = set(list2[i-1]).intersection(set(list2[f]))
                    num_common_elements = len(common_elements)
                    
                    # Find the total number of unique elements in both lists
                    total_elements = set(list2[i-1]).union(set(list2[f]))
                    num_total_elements = len(total_elements)
                    
                    # Calculate the percentage similarity
                    percentage_similarity = (num_common_elements / num_total_elements) * 100
                    
                    # Print the result
                    hypList.append(format(percentage_similarity))
                except ZeroDivisionError:
                     hypList.append(0.00)
            r=r+1
    print(hypList)
    ###############
    list3 = []
    for key3 in dic3:
        list3.append(dic3[key3])
    b = len(list3)
    u = 1
    hoList = []
    for i in range(1, b):
            for f in range(u, b):
                try: 
                    common_elements = set(list3[i-1]).intersection(set(list3[f]))
                    num_common_elements = len(common_elements)
                    
                    # Find the total number of unique elements in both lists
                    total_elements = set(list3[i-1]).union(set(list3[f]))
                    num_total_elements = len(total_elements)
                    
                    # Calculate the percentage similarity
                    percentage_similarity = (num_common_elements / num_total_elements) * 100
                    
                    # Print the result
                    hoList.append(format(percentage_similarity))
                except ZeroDivisionError:
                     hoList.append(0.00)
            u=u+1
    print(hoList)

    r = len(listS)
    u = 1
    SList = []
    for i in range(1, r):
            for f in range(u, r):
                try: 
                    common_elements = set(listS[i-1]).intersection(set(listS[f]))
                    num_common_elements = len(common_elements)
                    
                    # Find the total number of unique elements in both lists
                    total_elements = set(listS[i-1]).union(set(listS[f]))
                    num_total_elements = len(total_elements)
                    
                    # Calculate the percentage similarity
                    percentage_similarity = (num_common_elements / num_total_elements) * 100
                    
                    # Print the result
                    SList.append(format(percentage_similarity))
                except ZeroDivisionError:
                     SList.append(0.00)
            u=u+1
    print(SList)
##call percent to run
percent()
##synList
##hypList
##hoList
##SList
