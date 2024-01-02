import spacy
import pandas as pd

nlp = spacy.load('en_core_web_sm')

def extract_noun_phrases(df, text_column):
    noun_phrases_list = []
    for index, row in df.iterrows():
        doc = nlp(row[text_column])
        noun_phrases = [chunk.text for chunk in doc.noun_chunks]
        noun_phrases_list.append(noun_phrases)
    return noun_phrases_list

# Example usage:
# Assuming you have a DataFrame df with a text column named 'text_column'
# noun_phrases = extract_noun_phrases(df, 'text_column')
