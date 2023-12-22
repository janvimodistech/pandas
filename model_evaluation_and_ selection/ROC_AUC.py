import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score

def evaluate_gradient_boosting_classifier(data):
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = GradientBoostingClassifier()
    clf.fit(X_train, y_train)
    y_probs = clf.predict_proba(X_test)[:, 1]

    # Calculate the ROC-AUC score
    roc_auc = roc_auc_score(y_test, y_probs)

    return roc_auc

