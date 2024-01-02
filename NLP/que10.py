import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tag_document(text):
    words = word_tokenize(text)
    pos_tags = nltk.pos_tag(words)

    return pos_tags
text = "The quick brown fox jumps over the lazy dog."
pos_tags = pos_tag_document(text)
print(pos_tags)
