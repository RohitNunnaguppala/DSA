import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')

def find_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)

word = "happy"
synonyms = find_synonyms(word)
print(f"Synonyms for {word}: {synonyms}")