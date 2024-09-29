"""1. Install matplotlib  & you can use plt.plot() to create a line plot of given data

x = [0, 5, 9, 10, 15, 20, 25] 

y = [0, 1, 2, 3, 4, 5, 6]"""

import matplotlib.pyplot as plt

# Given data
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Creating a line plot
plt.plot(x, y)

# Adding title and labels
plt.title('Line Plot of x vs y')
plt.xlabel('x values')
plt.ylabel('y values')

# Display the plot
plt.show()
