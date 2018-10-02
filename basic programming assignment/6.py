"""
Python basics assignment 6: Dictionary
Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should covert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than a-z. Compare your results with https://en.wikipedia.org/wiki/Letter_frequency - 2 points

Solution by Jamison Lahman, June 1, 2017
"""

import string

counts = 0
dictionary_counts = dict()                       #Initializes the dictionary
fname = input('Enter file name: ')
with open(fname) as fhand:     # Use context manager to open file
    for line in fhand:
        line = line.translate(str.maketrans('', '', string.digits))
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        #Removes numbers then punctuation, and lower cases the letters
        words = line.split()
        for word in words:
            for letter in word:
                counts += 1          #counts each letter for relative frequencies
                if letter not in dictionary_counts:
                    dictionary_counts[letter] = 1
                else:
                    dictionary_counts[letter] += 1
                    
    relative_lst = list()           #Initializes the list
    for key, val in list(dictionary_counts.items()):
        relative_lst.append((val/counts,key))    #Computes the relative frequency
        
    relative_lst.sort(reverse=True)             #Sorts from highest rel freq

    for key, val in relative_lst:                
        print(key,val)