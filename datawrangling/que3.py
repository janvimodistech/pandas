import pandas as pd

# Create sample DataFrames
data1 = {'key': ['A', 'B', 'C', 'D'],
         'value1': [1, 2, 3, 4]}
data2 = {'key': ['B', 'D', 'E', 'F'],
         'value2': [5, 6, 7, 8]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# Merge df1 and df2 on the 'key' column
merged_df = pd.merge(df1, df2, on='key', how='inner')
print(merged_df)
