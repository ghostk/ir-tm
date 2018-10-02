"""
Python basics assignment 5: String
Use str.find and str.rfind method () to extract an email address from a string (if there are multiple emails, please extract the first one). - 2 points

Solution by Kun Lu, September 28, 2018
"""


data = input('Please type in a sentence containing an email address: ')
atpos = data.find('@')
if atpos == -1:
    print('no email address is found from your sentence')
else:
    endpos = data.find(' ', atpos)
    startpos = data.rfind(' ', 0, atpos)
    if endpos == -1:
        email = data[startpos + 1:]
    else:
        email = data[startpos + 1: endpos]
    print (email)
    