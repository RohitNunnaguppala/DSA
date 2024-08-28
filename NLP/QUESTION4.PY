def tokenize_whitespace(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        tokens = content.split()
        print(tokens)
    
    except FileNotFoundError:
        print(f"File {file_path} not found")
        
tokenize_whitespace('sample1.txt')