#1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

def div(a, b):
    # Check if the second number is not zero to avoid division by zero error
    if b != 0:
        result = a / b
        print(f"The division of {a} by {b} is: {result}")
    else:
        print("Division by zero is not allowed.")

# Call the function with two numbers
div(10, 2)  # Example: 10 divided by 2

#Ans: The division of 10 by 2 is: 5.0
