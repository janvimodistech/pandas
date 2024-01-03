import pandas as pd

# Create a sample DataFrame with duplicate rows
data = {'A': [1, 1, 2, 2, 3],
        'B': ['x', 'x', 'y', 'y', 'z']}
df = pd.DataFrame(data)

# Remove duplicate rows based on all columns
df_no_duplicates = df.drop_duplicates()

# Remove duplicate rows based on a subset of columns
df_no_duplicates_subset = df.drop_duplicates(subset=['A'])

print("DataFrame with duplicate rows:")
print(df)
print("\nDataFrame with no duplicate rows (based on all columns):")
print(df_no_duplicates)
print("\nDataFrame with no duplicate rows (based on subset of columns):")
print(df_no_duplicates_subset)
