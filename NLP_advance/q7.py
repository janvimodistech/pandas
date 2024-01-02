import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess
data = {
    'text': ['The quick brown fox', 'Jumps over the lazy dog'],
    'label': [0, 1]  
}
df = pd.DataFrame(data)
sentences = [simple_preprocess(text) for text in df['text']]
word2vec_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
X = [word2vec_model.wv[sentence] for sentence in sentences]
X_train, X_test, y_train, y_test = train_test_split(X, df['label'], test_size=0.2, random_state=42)
classifier = SVC()
classifier.fit(X_train, y_train)
accuracy = classifier.score(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')
