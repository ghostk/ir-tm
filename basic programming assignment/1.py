"""
Python basics assignment 1: Variables and Expressions
Write a Python program which prompts the user for a weight in pounds, and convert the weight to kilograms, and print out the converted weight. - 2 points

Enter weight in Pounds:1
The weight in Kilograms is:0.4536

Solution by Kun Lu, September 28, 2018
"""

input_weight = input('Enter weight in Pounds: ')
try:
    weight = float(input_weight)
    kg_weight = weight * 0.4536
    print ('The weight in Kilograms is:', kg_weight)
except:
    print('Please enter a number')