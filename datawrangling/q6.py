import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Rename columns
new_column_names = {'A': 'First Column', 'B': 'Second Column'}
df = df.rename(columns=new_column_names)

# Display the DataFrame with renamed columns
print(df)
