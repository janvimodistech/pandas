import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

def lemmatize_document(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Initialize WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()

    # Lemmatize each word in the text
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

    # Join the lemmatized words back into a single string
    lemmatized_text = ' '.join(lemmatized_words)

    return lemmatized_text

# Example usage:
text = "The dogs are barking loudly outside. I am running in the park."
lemmatized_text = lemmatize_document(text)
print("Original text:")
print(text)
print("\nLemmatized text:")
print(lemmatized_text)
