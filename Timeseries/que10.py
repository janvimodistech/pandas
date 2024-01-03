import pandas as pd
import matplotlib.pyplot as plt
data = [10, 15, 12, 14, 100, 13, 12, 11, 12, 14, 13, 12, 16, 12, 11, 12, 13, 14, 12, 11, 15]
index = pd.date_range('2023-01-01', periods=len(data), freq='D')
time_series = pd.Series(data, index=index)
z_scores = (time_series - time_series.mean()) / time_series.std()
threshold = 3
outliers = time_series[abs(z_scores) > threshold]
time_series_cleaned = time_series.drop(outliers.index)
plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Original')
plt.plot(time_series_cleaned, label='Cleaned', linestyle='--', marker='o')
plt.scatter(outliers.index, outliers.values, color='r', label='Outliers')
plt.title('Time Series with Outliers')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()
