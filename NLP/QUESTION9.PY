import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

def find_hypernyms_hyponyms(word):
    
    hypernyms = []
    hyponyms = []
    
    for syn in wordnet.synsets(word):
        for hyper in syn.hypernyms():
                hypernyms.extend(hyper.lemma_names())
        for hypo in syn.hyponyms():
                hyponyms.extend(hypo.lemma_names())
                
    return set(hypernyms), set(hyponyms)

word = "dog"

hypernyms,hyponyms = find_hypernyms_hyponyms(word)
print("Hypernyms of",word,":",hypernyms)
print("Hyponyms of",word,":",hyponyms)