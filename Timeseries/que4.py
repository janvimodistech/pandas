import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
data = [3, 5, 4, 6, 8, 7, 9, 10, 12, 11, 13, 15, 14, 16, 18, 17, 19, 21, 20, 22]
index = pd.date_range('2023-01-01', periods=len(data), freq='W')
time_series = pd.Series(data, index=index)
decomposition = seasonal_decompose(time_series, model='additive', period=4)  
fig, axes = plt.subplots(4, 1, figsize=(12, 10))
axes[0].plot(time_series, label='Original')
axes[0].set_title('Original Time Series')

# Plot the trend component
axes[1].plot(decomposition.trend, label='Trend', color='b')
axes[1].set_title('Trend Component')

# Plot the seasonal component
axes[2].plot(decomposition.seasonal, label='Seasonal', color='g')
axes[2].set_title('Seasonal Component')

# Plot the residual component
axes[3].plot(decomposition.resid, label='Residual', color='r')
axes[3].set_title('Residual Component')
plt.tight_layout()
plt.show()
