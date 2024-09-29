"""2.Visualize the daily temperature changes over time in a city and give your conclusion

 Input: days = list(range(1, 32)) 

# Daily temperature data (replace with your own data) 

temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80,
81, 82, 83, 82, 80, 78, 76, 74, 71]"""

import matplotlib.pyplot as plt

# Data for visualization
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create a line plot to visualize temperature changes over time
plt.figure(figsize=(10, 6))
plt.plot(days, temperature, color='orange', marker='o')

# Adding titles and labels
plt.title('Daily Temperature Changes Over Time')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°F)')

# Show the plot
plt.grid(True)
plt.show()
