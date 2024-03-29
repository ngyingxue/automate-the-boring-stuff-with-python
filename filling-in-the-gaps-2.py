'''
Filling in the Gaps
As an added challenge, write another program that can insert gaps into
numbered files so that a new file can be added.
'''

import os, re, shutil
from pathlib import Path

directory = Path(input('Enter directory\n'))
prefix = input('Enter prefix\n')
fillin = int(input('Enter number to fill in\n'))

files = []
maxLength = 0
numbers = []
newlist = []

for filename in os.listdir(directory):

    if filename.startswith(prefix):
        files.append(filename)
        match = re.search(rf'({re.escape(prefix)})(\d+)(.*)', filename)
        matchNumber = re.search(r'(0*)(\d+)', match.group(2))
        numbers.append(int(matchNumber.group(2)))

for i in numbers:
    if i >= fillin:
        i += 1
        length = len(str(i))
        if length > maxLength:
            maxLength = length
    newlist.append(i)

files.sort(reverse=True)
newlist.sort(reverse=True)

for x, y in zip(files, newlist):
    match = re.search(rf'({re.escape(prefix)})(\d+)(.*)', x)
    suffix = match.group(3)
    numberFormatted = str(y).zfill(maxLength)
    newFilename = prefix+numberFormatted+suffix
    oldpath = os.path.join(directory,x)
    newpath = os.path.join(directory,newFilename)
    print(x, newFilename)
    shutil.move(oldpath,newpath)
