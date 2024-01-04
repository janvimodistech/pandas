import pandas as pd
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
data = {'Date': date_range, 'Value': range(len(date_range))}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)
weekly_resampled = df.resample('W').mean()
print(weekly_resampled)
