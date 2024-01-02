import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import re
nltk.download('punkt')
with open('removenum.txt', 'r', encoding='utf-8') as file:
    text = file.read()
sentences = sent_tokenize(text)
cleaned_sentences = []
for sentence in sentences:
    words = word_tokenize(sentence)
    words = [word for word in words if not re.match(r'^-?\d+(?:\.\d+)?1233455$', word)]
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
for sentence in cleaned_sentences:
    print(sentence)
