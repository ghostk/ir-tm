"""
Python basics assignment 9: File, String and Dictionary
Download the example text directory from Canvas. Use os.scandir(path) method to read all text files in the directory. Write a program to save words and their counts aggregated across all these text files to 'wordcounts.txt'. - 2 points

Solution by Kun Lu, September 28, 2018
"""


import glob, string

counts = dict()
for fname in glob.glob('texts/*.txt'):
    with open(fname) as f:
        for line in f:
            line = line.translate(line.maketrans('', '', string.punctuation))
            line = line.lower()
            words = line.split()
            for word in words:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1

with open('wordcounts.txt', 'w') as fout:           
    for word in counts:
        fout.write(word + " " + str(counts[word]) + "\n")