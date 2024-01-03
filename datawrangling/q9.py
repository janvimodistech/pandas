import pandas as pd
data = {
    'group': ['A', 'B', 'A', 'B', 'A', 'B'],
    'value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)
summary_statistics = df.groupby('group')['value'].agg(['mean', 'median', 'std'])
print(summary_statistics)
