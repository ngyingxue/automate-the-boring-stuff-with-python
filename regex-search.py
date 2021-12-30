'''
Regex Search
Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should be
printed to the screen.
'''

from pathlib import Path
import re

directory = Path(input('Enter a directory\n'))
openDirectory = list(directory.glob('*.txt'))

print(openDirectory)

expression = input('Enter a regular expression\n')

matches =[]

for i in openDirectory:
    openFile = open('%s' % i ,'r')
    text = openFile.read()
    check = re.findall(r'%s' % expression, text)
    if check != []:
        matches.append(check)

if matches != []:
    print(matches)
