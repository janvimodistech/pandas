import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
data = [3, 5, 4, 6, 8, 7, 9, 10, 12, 11, 13, 15, 14, 16, 18, 17, 19, 21, 20, 22]
index = pd.date_range('2023-01-01', periods=len(data), freq='W')
time_series = pd.Series(data, index=index)
decomposition = seasonal_decompose(time_series, model='additive', period=4)

# Plot the trend component
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(decomposition.trend, label='Trend', color='b')
plt.title('Trend Component')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

# Plot the seasonal component
plt.subplot(412)
plt.plot(decomposition.seasonal, label='Seasonal', color='g')
plt.title('Seasonal Component')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

# Plot the residual component
plt.subplot(413)
plt.plot(decomposition.resid, label='Residual', color='r')
plt.title('Residual Component')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

# Plot the original time series
plt.subplot(414)
plt.plot(time_series, label='Original', color='k')
plt.title('Original Time Series')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()

plt.tight_layout()
plt.show()
