import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')

def remove_stopwords(text):
  
    stop_words = set(stopwords.words('english'))
  
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    words = text.split()
  
    filtered_words = [word for word in words if word not in stop_words]
    
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text

if __name__ == "__main__":
    text_document = "This is a sample text document it contains some words"
    
    cleaned_text = remove_stopwords(text_document)
    print(cleaned_text)
