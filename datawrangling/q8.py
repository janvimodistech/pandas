import pandas as pd

# Sample DataFrame
data = {
    'group': ['A', 'B', 'A', 'B', 'A', 'B'],
    'value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# Function to calculate summary statistics for different groups
def calculate_summary_statistics(df, group_column, value_column):
    # Group the DataFrame by the specified column(s)
    grouped_df = df.groupby(group_column)
    
    # Calculate summary statistics for each group
    summary_statistics = grouped_df[value_column].agg(['mean', 'median', 'min', 'max', 'std', 'count'])
    
    return summary_statistics

# Call the function to calculate summary statistics
result = calculate_summary_statistics(df, 'group', 'value')
print(result)
