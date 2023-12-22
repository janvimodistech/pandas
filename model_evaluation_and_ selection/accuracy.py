import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
df = pd.read_csv('Churn_Modelling.csv')
print(df.info())
X = df.drop(columns=["Exited", "RowNumber", "CustomerId", "Surname", "Geography", "Gender"])  # Exclude non-numeric and non-essential columns
y = df["Exited"]

# X = df.iloc[:, :-1] 
# y = df.iloc[:, -1]   
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
