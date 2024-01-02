import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Sample document
document = """
NLTK is a leading platform for building Python programs to work with human language data. 
It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, 
along with a suite of text processing libraries for classification, tokenization, stemming, 
tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, 
and an active discussion forum.
"""

def count_word_frequency(document):  
    words = word_tokenize(document)
    word_freq = Counter(words)

    return word_freq

def main():
    nltk.download('punkt')
    word_freq = count_word_frequency(document)
    print("Word Frequency:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
