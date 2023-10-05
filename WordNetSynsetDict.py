from nltk.corpus import wordnet  #import Wordnet and the Natural Language Toolkit
print("Enter words all lowercase with a single space in between (ex: fun tool love)")
inp = input("What are the words you want synonyms for? ")
inps = inp.split(' ')
def findSynonyms():
    dict = {}
    for h in inps:  #loop through each word in our input, finding the synonyms and adding them to a list. Add that list to a dictionary with the key being the word itself
        synonyms = [] 
        for syn in wordnet.synsets(h):
            for i in syn.lemmas():
                synonyms.append(i.name())
                dict.update({h:synonyms})
    print(dict)
def findHyper():
    hyperDict = {}
    for word in inps:
        My_sysn = wordnet.synsets(word)[0]
        hyperDict.update({word : My_sysn.hypernyms()})

def findHypo():
    hypoDict = {}
    for word in inps:
        My_sysn = wordnet.synsets(word)[0]
        hypoDict.update({word : My_sysn.hyponyms()})
