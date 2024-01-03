import pandas as pd
data = {'category': ['A', 'B', 'C', 'A', 'C']}
df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df, columns=['category'])
print("Original DataFrame:")
print(df)
print("\nDataFrame after one-hot encoding:")
print(df_encoded)
