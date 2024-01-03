import pandas as pd
data = {'A': [1, 2, None, 4],
        'B': [5, None, 7, 8]}
df = pd.DataFrame(data)
cleaned_df = df.dropna()
cleaned_df.to_csv('cleaned_data.csv', index=False)
