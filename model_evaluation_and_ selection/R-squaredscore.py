import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
diabetes = load_diabetes()
df = pd.DataFrame(data=np.c_[diabetes['data'], diabetes['target']],
                  columns=diabetes['feature_names'] + ['target'])
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r_squared = r2_score(y_test, y_pred)
print(f"R-squared score: {r_squared:.4f}")
