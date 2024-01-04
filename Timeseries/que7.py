import pandas as pd
import matplotlib.pyplot as plt
data = [3, 5, 4, 6, 8, 7, 9, 10, 12, 11, 13, 15, 14, 16, 18, 17, 19, 21, 20, 22]
index = pd.date_range('2023-01-01', periods=len(data), freq='W')
time_series = pd.Series(data, index=index)
moving_avg = time_series.rolling(window=3).mean()
plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Original Time Series', color='b')
plt.plot(moving_avg, label='Moving Average (Window=3)', color='r')
plt.title('Moving Average of a Time Series')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()
