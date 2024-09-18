"""2. Convert the below list into a numpy array then display the array then
display the first and last index and then multiply each element by 2 and display the result.

 Input: my_list = [1, 2, 3, 4, 5]"""

import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert list to numpy array
my_array = np.array(my_list)

# Display the first and last index
first_element = my_array[0]
last_element = my_array[4]

print("Array:", my_array)
print("First element:", first_element)
print("Last element:", last_element)

# Multiply each element by 2
multiplied_array = my_array * 2
print("Array multiplied by 2:", multiplied_array)

"""Ans:Array: [1 2 3 4 5]
First element: 1
Last element: 5
Array multiplied by 2: [ 2  4  6  8 10]"""
