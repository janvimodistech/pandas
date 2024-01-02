import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')
text = "The quick brown fox jumps over the lazy dog."
doc = nlp(text)
for sent in doc.sents:
    for token in sent:
        print(token.text, token.dep_, token.head.text)
    print('\n')
