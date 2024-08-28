def normalize_text(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            content = file.read()
        normalize_content = content.lower()
        print(normalize_content)
    
    except FileNotFoundError:
        print(f"File {file_path} not found")
        
normalize_text('sample1.txt')