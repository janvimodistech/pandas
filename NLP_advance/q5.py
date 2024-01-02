import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
def extract_keywords(text):
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer(max_features=10)  # Adjust max_features as needed

    # Fit the vectorizer to the text data and transform the text into TF-IDF features
    tfidf_matrix = vectorizer.fit_transform([text])

    # Get the feature names (keywords) from the vectorizer
    feature_names = vectorizer.get_feature_names_out()

    # Create a dictionary to store the keywords and their corresponding TF-IDF scores
    keywords = {}
    for col in tfidf_matrix.nonzero()[1]:
        keywords[feature_names[col]] = tfidf_matrix[0, col]

    
    keywords = dict(sorted(keywords.items(), key=lambda item: item[1], reverse=True))

    return keywords

text = """
Natural Language Processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of human–computer interaction. Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation.
NLP can be used to analyze text, allowing machines to understand how human language works. This includes tasks such as language translation, sentiment analysis, text summarization, and more. NLP techniques are widely used in applications like virtual assistants, chatbots, search engines, and language translation services.
"""

keywords = extract_keywords(text)
print(keywords)
