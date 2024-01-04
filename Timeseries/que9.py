import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
data = [3, 5, 4, 6, 8, 7, 9, 10, 12, 11, 13, 15, 14, 16, 18, 17, 19, 21, 20, 22]
index = pd.date_range('2023-01-01', periods=len(data), freq='W')
time_series = pd.Series(data, index=index)
plt.figure(figsize=(12, 6))
plot_acf(time_series, lags=10, ax=plt.gca())
plt.title('Autocorrelation Function (ACF)')
plt.xlabel('Lag')
plt.ylabel('ACF')
plt.show()
plt.figure(figsize=(12, 6))
plot_pacf(time_series, lags=10, ax=plt.gca())
plt.title('Partial Autocorrelation Function (PACF)')
plt.xlabel('Lag')
plt.ylabel('PACF')
plt.show()
