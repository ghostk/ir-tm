"""
Python basics assignment 10: File, String and Regular Expression
Download the example csv file from Canvas. Extract all hyperlinks from the “text” column and print them out.

Solution by Kun Lu, September 28, 2018
"""

import csv, re
with open('dataset.csv', newline='') as f:
    freader = csv.reader(f, dialect='excel')
    for row in freader:
        text = row[3]
        links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        for link in links:
            print (link)