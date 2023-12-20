import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sgd_classifier = SGDClassifier(random_state=42)
sgd_classifier.fit(X_train, y_train)
y_pred = sgd_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_report_result = classification_report(y_test, y_pred, zero_division=1)  # Set zero_division=1 to avoid warnings
print(f'Accuracy: {accuracy:.2f}\n')
print('Classification Report:\n', classification_report_result)
