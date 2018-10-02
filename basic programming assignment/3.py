"""
Python basics assignment 3: Functions
Rewrite the program from 2, and use a function called computegrade that takes a score as its parameter and returns a grade as a string. It should provide the same output as 2. - 2 points

Solution by Kun Lu, September 28, 2018
"""

def computegrade(score):
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
        
input_score = input('Enter score: ')
try:
    score = float(input_score)
except:
    print('Bad score')
    quit()
# Use the computegrade() function
computegrade(score)