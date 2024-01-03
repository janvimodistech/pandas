import pandas as pd

# Create a sample DataFrame with daily time series data
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
data = {'Date': date_range, 'Value': range(len(date_range))}
df = pd.DataFrame(data)

# Convert the 'Date' column to the index of the DataFrame
df.set_index('Date', inplace=True)

# Resample the data from daily to weekly frequency and calculate the mean for each week
weekly_resampled = df.resample('W').mean()

# Print the weekly resampled data
print(weekly_resampled)
