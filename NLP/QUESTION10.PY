# Import necessary libraries
import nltk
from nltk.corpus import treebank

# Download TreeBank data if not already downloaded
nltk.download('treebank')
nltk.download('averaged_perceptron_tagger')

# Function to perform part-of-speech tagging using TreeBank
def pos_tagging(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged_tokens = nltk.pos_tag(tokens)
    return tagged_tokens

# Example usage
sentence = "The quick brown fox jumps over the lazy dog."
tagged_sentence = pos_tagging(sentence)
print(tagged_sentence)
