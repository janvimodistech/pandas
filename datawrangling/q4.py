import pandas as pd

def merge_and_save_csv(df1, df2, key, output_file):
    merged_df = pd.merge(df1, df2, on=key)
    merged_df.to_csv(output_file, index=False)

# Example usage
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
merge_and_save_csv(df1, df2, 'key', 'merged_data.csv')
