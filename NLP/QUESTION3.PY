from collections import Counter
def word_frequencies(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            content = file.read()
        words = content.split() 
        frequency = Counter(words)
        for word, freq in frequency.items():
            print(f"{word} {freq}")
    
    except FileNotFoundError:
        print((f"File {file_path} not found"))
        
word_frequencies('sample1.txt')