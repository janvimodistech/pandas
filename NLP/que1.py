import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Tokenize sentences and words in a text file
file_path = r"D:\pandas\pandas\NLP\input.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize sentences
sentences = sent_tokenize(text)

# Tokenize words in each sentence
tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

# Print tokenized sentences and words
print("Tokenized Sentences:")
for sentence in tokenized_sentences:
    print(sentence)
