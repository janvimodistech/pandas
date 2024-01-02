import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
text = "Stemming is a technique used to reduce words to their word stem or root form."
tokens = word_tokenize(text)
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]
stemmed_text = ' '.join(stemmed_words)
print("Stemmed Text:")
print(stemmed_text)
