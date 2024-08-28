import re

def clean_and_tokenize(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    words = text.split()
    
    return words


if __name__ == "__main__":
   
    file_path = 'sample1.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text_document = file.read()
    tokens = clean_and_tokenize(text_document)

    print(tokens)
