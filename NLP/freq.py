import re
from collections import Counter

def word_frequency_counter(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    words = text.split()
    word_freq = Counter(words)
    
    return dict(word_freq)

if __name__ == "__main__":
    
    file_path = 'sample1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text_document = file.read()
    word_freq_dict = word_frequency_counter(text_document)

    print(word_freq_dict)