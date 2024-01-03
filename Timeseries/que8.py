import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL

def generate_stl_decomposition(time_series, seasonal=13):
    """
    Generate a time series decomposition using STL (Seasonal-Trend decomposition using LOESS).
    
    Args:
    - time_series (pd.Series): The input time series.
    - seasonal (int): The seasonal periodicity. Default is 13 (for monthly data).
    
    Returns:
    - decomposition (STLResult): The result of the STL decomposition.
    """
    # Perform STL decomposition
    stl = STL(time_series, seasonal=seasonal)
    decomposition = stl.fit()
    
    return decomposition

# Example usage
# Create a sample time series (replace this with your actual data)
data = [3, 5, 4, 6, 8, 7, 9, 10, 12, 11, 13, 15, 14, 16, 18, 17, 19, 21, 20, 22]
index = pd.date_range('2023-01-01', periods=len(data), freq='W')
time_series = pd.Series(data, index=index)

# Generate STL decomposition
stl_decomposition = generate_stl_decomposition(time_series)

# Plot the STL decomposition
plt.figure(figsize=(12, 8))

plt.subplot(411)
plt.plot(time_series, label='Original Time Series')
plt.legend()

plt.subplot(412)
plt.plot(stl_decomposition.trend, label='Trend Component', color='b')
plt.legend()

plt.subplot(413)
plt.plot(stl_decomposition.seasonal, label='Seasonal Component', color='g')
plt.legend()

plt.subplot(414)
plt.plot(stl_decomposition.resid, label='Residual Component', color='r')
plt.legend()

plt.tight_layout()
plt.show()
