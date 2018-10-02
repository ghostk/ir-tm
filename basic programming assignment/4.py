"""
Python basics assignment 4: Iteration
Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the count, sum, maximum, minimum, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number. - 2 points

Solution by Kun Lu, September 28, 2018
"""

count = 0
sum = 0
avg = 0
max = None
min = None

while True:
    input1 = input('Enter a number, when you are done, enter done: ')
    if input1 == 'done': break   #Exits loop
    try:
        number = float(input1)
    except:
        print('Invalid input')
        continue
    if max is None or number > max: #Condition for max
        max = number
    if min is None or number < min: #Condition for min
        min = number
    count = count + 1
    sum = sum + number
avg = sum/count
print("The total valid numbers entered is:", count)
print("The sum is:", sum)
print("The maximum is:", max)
print("The minimum is:", min)
print("The average is:", avg)