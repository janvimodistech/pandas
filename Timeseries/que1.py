import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('daily-minimum-temperatures-in-me.csv')
print(df.columns)

# Convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Plot the time series data if the column name is correct
if 'Daily minimum temperatures' in df.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Daily minimum temperatures'], label='Minimum Daily Temperatures')
    plt.title('Minimum Daily Temperatures in Melbourne, Australia')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.show()
else:
    print("Column 'Daily minimum temperatures' not found in the DataFrame.")
