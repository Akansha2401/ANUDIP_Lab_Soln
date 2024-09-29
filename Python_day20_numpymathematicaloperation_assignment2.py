"""2. Calculate the profit made by a company

 Input: revenue = np.array([10000, 12000, 11000, 10500]) 

expenses = np.array([4000, 5000, 4500, 4800])

 Output: Profit: [6000 7000 6500 5700]"""

import numpy as np

# Input arrays for revenue and expenses
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Use NumPy's subtraction operation for element-wise subtraction
profit = np.subtract(revenue, expenses)

print("Profit:",profit)

#Ans:Profit: [6000 7000 6500 5700]

