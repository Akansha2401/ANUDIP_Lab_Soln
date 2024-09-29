"""1.Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 

Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 

# Monthly expenses in dollars (replace with your own data) 

expenses = [1200, 400, 200, 150, 250]"""

import matplotlib.pyplot as plt

# Data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(categories, expenses, color='skyblue')

# Adding titles and labels
plt.title('Monthly Expenses by Category')
plt.xlabel('Spending Categories')
plt.ylabel('Expenses (in dollars)')

# Show the plot
plt.show()
