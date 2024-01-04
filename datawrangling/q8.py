import pandas as pd
data = {
    'group': ['A', 'B', 'A', 'B', 'A', 'B'],
    'value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)
def calculate_summary_statistics(df, group_column, value_column):
    grouped_df = df.groupby(group_column)
    summary_statistics = grouped_df[value_column].agg(['mean', 'median', 'min', 'max', 'std', 'count'])
    return summary_statistics
result = calculate_summary_statistics(df, 'group', 'value')
print(result)
