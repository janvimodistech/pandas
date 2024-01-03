import pandas as pd
data = {'A': [1, 2, None, 4], 'B': [5, None, 7, 8]}
df = pd.DataFrame(data)
df_dropped_rows = df.dropna()
df_dropped_columns = df.dropna(axis=1)
print("DataFrame with dropped rows:")
print(df_dropped_rows)

print("\nDataFrame with dropped columns:")
print(df_dropped_columns)
