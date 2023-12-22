import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
iris = datasets.load_iris()
X = iris.data
y = iris.target
svm_classifier = SVC(kernel='linear', C=1)
scores = cross_val_score(svm_classifier, X, y, cv=5)
print(f"Cross-validation scores: {scores}")
print(f"Mean accuracy: {np.mean(scores):.2f}")
