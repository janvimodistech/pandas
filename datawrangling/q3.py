import pandas as pd
data = {'A': [1, 2, None, 4, 5],
        'B': [None, 2, 3, 4, 5],
        'C': [1, 2, 3, 4, None]}
df = pd.DataFrame(data)
mean_filled_df = df.fillna(df.mean())
median_filled_df = df.fillna(df.median())

print("Original DataFrame:")
print(df)
print("\nDataFrame with missing values filled using mean:")
print(mean_filled_df)
print("\nDataFrame with missing values filled using median:")
print(median_filled_df)
