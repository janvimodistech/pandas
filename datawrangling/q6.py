import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
new_column_names = {'A': 'First Column', 'B': 'Second Column'}
df = df.rename(columns=new_column_names)
print(df)
