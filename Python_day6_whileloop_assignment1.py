#1.Write a python program to check whether a number is palindrome or not? 

def is_palindrome(number):
    """
    Function to check if a number is a palindrome.
    
    Parameters:
    - number (int): The number to check.

    Returns:
    - bool: True if the number is a palindrome, False otherwise.
    """
    # Convert the number to a string to check for palindrome property
    number_str = str(number)
    
    # Compare the original string with its reverse
    return number_str == number_str[::-1]

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is a palindrome and display the result
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

"""Ans: Enter a number: 24
24 is not a palindrome.
Enter a number: 121
121 is a palindrome."""
