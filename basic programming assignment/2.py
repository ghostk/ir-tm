"""
Python basics assignment 2: Conditional execution
Write a Python program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table: - 2 points

Enter score: 0.95
A+
Enter score: perfect
Bad score
Enter score: 10.0
Bad score

Solution by Kun Lu, September 28, 2018
"""


input1 = input('Enter score: ')
try:
    score = float(input1)
except:
    print('Bad score')
    quit()

if score > 0 and score < 1:
    if score >= .95:
        print('A+')
    elif score >= .9:
        print('A')
    elif score >= .85:
        print('B+')
    elif score >= .8:
        print('B')
    elif score >= .75:
        print('C+')
    elif score >= .7:
        print('C')
    elif score >= .65:
        print('D+')
    elif score >= .6:
        print('D')
    else:
        print('F')
else:
    print('Bad score')
    


    