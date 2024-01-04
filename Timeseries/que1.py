import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('daily-minimum-temperatures-in-me.csv')
print(df.columns)
df['Date'] = pd.to_datetime(df['Date'])
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
