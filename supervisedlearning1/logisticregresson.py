import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "D:\jupiternb\Churn_Modelling.csv"
df = pd.read_csv(file_path)
print(df.head())
print(df.isnull().sum())
X = df.drop(['RowNumber', 'CustomerId', 'Surname', 'Exited'], axis=1)  # Exclude non-numeric and target columns
y = df['Exited']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
#  one-hot encoding for categorical variables
X_train_encoded = pd.get_dummies(X_train, columns=['Geography', 'Gender'], drop_first=True)

print(X_train_encoded.head())
model = LogisticRegression()
model.fit(X_train_encoded, y_train)
X_test_encoded = pd.get_dummies(X_test, columns=['Geography', 'Gender'], drop_first=True)
y_pred = model.predict(X_test_encoded)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Confusion Matrix:')
print(conf_matrix)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()