import pandas as pd
import matplotlib.pyplot as plt
try:
    df = pd.read_csv('daily-minimum-temperatures-in-me.csv')
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit(1)
print(df.head())
df['Date'] = pd.to_datetime(df['Date'])
try:
    df['Daily minimum temperatures'] = pd.to_numeric(df['Daily minimum temperatures'], errors='coerce')
except KeyError:
    print("Column 'Daily minimum temperatures' not found in the DataFrame.")
    exit(1)
df = df.dropna(subset=['Daily minimum temperatures'])
rolling_mean = df['Daily minimum temperatures'].rolling(window=30).mean()
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Daily minimum temperatures'], label='Original Data')
plt.plot(df['Date'], rolling_mean, label='30-Day Rolling Mean', color='red')
plt.title('Rolling Mean of Daily Minimum Temperatures')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()
