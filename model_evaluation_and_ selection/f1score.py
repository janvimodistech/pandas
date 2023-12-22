import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

def evaluate_random_forest(df):
    
    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  
    clf = RandomForestClassifier(random_state=42)

    clf.fit(X_train, y_train)

   
    y_pred = clf.predict(X_test)

   
    f1 = f1_score(y_test, y_pred)

    return f1
import pandas as pd
from sklearn.datasets import load_iris


iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target


f1_score = evaluate_random_forest(df)
print(f"F1-score: {f1_score:.4f}")
