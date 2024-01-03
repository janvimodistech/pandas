import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)

# Scaling numerical features (min-max scaling)
df_scaled = (df - df.min()) / (df.max() - df.min())

# Applying log transformation to numerical features
df_log = np.log(df)

# Printing the transformed DataFrames
print("Scaled DataFrame:")
print(df_scaled)
print("\nLog-transformed DataFrame:")
print(df_log)
