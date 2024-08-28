import re

def remove_punctuation(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        cleaned_content = re.sub(r'[^\w\s]', '', content)
        print(cleaned_content)
    except FileNotFoundError:
        print(f'File {file_path} not found')
 
remove_punctuation('sample1.txt')