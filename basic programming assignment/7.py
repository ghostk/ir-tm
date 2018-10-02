"""
Python basics assignment 7: Regular expression
use regular expression to extract all email address from "wos.txt", and write it to a file "emails.txt"

Solution by Kun Lu, September 28, 2018
"""

import re

all_emails = list()
with open('wos.txt', 'r') as f:
    for line in f:
        emails = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
        for email in emails:
            all_emails.append(email)

with open('emails.txt', 'w') as ef:
    for email in all_emails:
        ef.write(email + '\n')

