"""
Python basics assignment 8: File and String
Write a program to find the lines that mention "Hillary" or "Trump" from the example text file. Write those lines into separate files named "Hillary.txt" and "Trump.txt" (The text files are supplied) - 2 points

Solution by Kun Lu, September 28, 2018
"""


fname = input("Enter the file name: ")
hillary = list()
trump = list()
with open(fname, 'r') as f:
    for line in f:
        if line.find('Hillary') != -1:
            hillary.append(line)
        if line.find('Trump') != -1:
            trump.append(line)

if len(hillary) > 0:
    with open('Hillary.txt', 'w') as hf:
        for item in hillary:
            hf.write(item)

if len(trump) > 0:
    with open('Trump.txt', 'w') as tf:
        for item in trump:
            tf.write(item)
        