import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [22, 24, 23, 25, 26, 24, 23]

plt.figure(figsize=(10, 6))
plt.plot(days, temperatures, marker='o', linestyle='-')
plt.xlabel('Day of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Trend over a Week')
plt.grid(True)
plt.show()
