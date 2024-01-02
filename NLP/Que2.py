import string
import nltk
from nltk.tokenize import word_tokenize
text = "NLTK is a leading platform for ! building Python programs to work with human language data."
tokens = word_tokenize(text)
filtered_tokens = [token for token in tokens if token not in string.punctuation]
filtered_text = ' '.join(filtered_tokens)
print("Filtered Text:")
print(filtered_text)
