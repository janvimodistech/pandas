import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
try:
    df = pd.read_csv('daily-minimum-temperatures-in-me.csv')
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit(1)

# Print the first few rows of the DataFrame to verify its structure
print(df.head())

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Clean the 'Daily minimum temperatures' column by replacing non-numeric values with NaN
try:
    df['Daily minimum temperatures'] = pd.to_numeric(df['Daily minimum temperatures'], errors='coerce')
except KeyError:
    print("Column 'Daily minimum temperatures' not found in the DataFrame.")
    exit(1)

# Drop rows with NaN values in the 'Daily minimum temperatures' column
df = df.dropna(subset=['Daily minimum temperatures'])

# Calculate the rolling mean with a window size of 30
rolling_mean = df['Daily minimum temperatures'].rolling(window=30).mean()

# Plot the original time series data and the rolling mean
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Daily minimum temperatures'], label='Original Data')
plt.plot(df['Date'], rolling_mean, label='30-Day Rolling Mean', color='red')
plt.title('Rolling Mean of Daily Minimum Temperatures')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()
