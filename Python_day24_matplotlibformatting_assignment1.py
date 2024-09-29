import matplotlib.pyplot as plt

# Data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create a pie chart
plt.figure(figsize=(7, 7))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])

# Add a title
plt.title('Monthly Income Distribution by Source')

# Show the pie chart
plt.show()
