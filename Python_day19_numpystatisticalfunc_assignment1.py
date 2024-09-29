"""1.Compute the median of the flattened NumPy array 

   Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])"""

import numpy as np

# Input array
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

# Flatten the array 
x_flattened = x_odd.flatten()

# Compute the median of the flattened array
median_value = np.median(x_flattened)

print(f"Median of the array: {median_value}")

#Ans:Median of the array: 4.0
