def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content= file.read()
        words= content.split()
        print(f"Total words in file: {len(words)}")
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        
count_words('sample.txt')


