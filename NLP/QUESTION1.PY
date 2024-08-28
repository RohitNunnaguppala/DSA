def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print(content)
    
    except FileNotFoundError:
        print(f"File {file_path} not found")
        
read_file('sample1.txt')