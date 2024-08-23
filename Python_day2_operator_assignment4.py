# 4. Python program to find the area of a triangle whose sides are given

import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
# Calculate the semi-perimeter
s = (a + b + c) / 2
# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"The area of the triangle is {area}")

"""Ans:Enter side a: 3
Enter side b: 3
Enter side c: 5
The area of the triangle is 4.14578098794425"""
