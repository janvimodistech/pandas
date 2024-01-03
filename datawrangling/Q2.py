import pandas as pd
import matplotlib.pyplot as plt
data = {'A': [1, 2, 2, 3, 4, 4],
        'B': ['x', 'y', 'y', 'z', 'w', 'w']}
df = pd.DataFrame(data)
df_cleaned = df.drop_duplicates()

# Visualize the cleaned data
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title('Original Data')
plt.scatter(df.index, df['A'], label='A')
plt.scatter(df.index, df['B'], label='B')
plt.legend()

plt.subplot(1, 2, 2)
plt.title('Cleaned Data')
plt.scatter(df_cleaned.index, df_cleaned['A'], label='A')
plt.scatter(df_cleaned.index, df_cleaned['B'], label='B')
plt.legend()

plt.tight_layout()
plt.show()
