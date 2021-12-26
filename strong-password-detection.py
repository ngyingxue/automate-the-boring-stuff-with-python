'''
Strong Password Detection

Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong
password is defined as one that is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string against multiple regex patterns to
validate its strength.
'''

import re

def strongPassword(password):
    upper = re.compile(r'[A-Z]')
    lower = re.compile(r'[a-z]')
    oneDigit = re.compile(r'[0-9]')

    if len(password) < 8:
        print('Password requires at least eight characters')

    if lower.search(password) == None:
        print('Password must contain lowercase characters')

    if upper.search(password) == None:
        print('Password must contain uppercase characters')

    if oneDigit.search(password) == None:
        print('Password must contain at least one digit')

    else:
        print('Password is strong')

strongPassword('ABCDEFGh4')
