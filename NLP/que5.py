import nltk
from nltk.tokenize import blankline_tokenize

# File path with raw string
file_path = r"D:\pandas\pandas\NLP\para.txt"  # Replace with the actual file path

# Read the text file and tokenize paragraphs
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        paragraphs = blankline_tokenize(text)
        for i, paragraph in enumerate(paragraphs, 1):
            print(f"Paragraph {i}:")
            print(paragraph)
            print()
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
