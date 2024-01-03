import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
data = [3, 5, 4, 6, 8, 7, 9, 10, 12, 11, 13, 15, 14, 16, 18, 17, 19, 21, 20, 22]
index = pd.date_range('2023-01-01', periods=len(data), freq='W')
time_series = pd.Series(data, index=index)

# Plot the autocorrelation function (ACF)
plot_acf(time_series, lags=10)
plt.title('Autocorrelation Function (ACF)')
plt.show()

# Plot the partial autocorrelation function (PACF)
plot_pacf(time_series, lags=10)
plt.title('Partial Autocorrelation Function (PACF)')
plt.show()
