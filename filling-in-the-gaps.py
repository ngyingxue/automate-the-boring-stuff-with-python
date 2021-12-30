'''
Filling in the Gaps
Write a program that finds all files with a given prefix, such as
spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps
in the numbering (such as if there is a spam001.txt and spam003.txt but no
spam002.txt). Have the program rename all the later files to close this gap
'''

import os, re, shutil
from pathlib import Path

directory = Path(input('Enter directory\n'))
prefix = input('Enter prefix\n')

files = []
maxLength = 0

for filename in os.listdir(directory):
    if filename.startswith(prefix):
        files.append(filename)
        match = re.search(rf'({re.escape(prefix)})(\d+)(.*)', filename)
        number=match.group(2)
        matchNumber = re.search(r'(0*)(\d+)', number)
        length = len(matchNumber.group(2))
        if length > maxLength:
            maxLength = length


files.sort()
print(files)
number = 1

for filename in files:
    match = re.search(rf'({re.escape(prefix)})(\d+)(.*)', filename)
    suffix = match.group(3)
    numberFormatted = str(number).zfill(maxLength)
    newFilename = prefix+numberFormatted+suffix
    oldpath = os.path.join(directory,filename)
    newpath = os.path.join(directory,newFilename)
    shutil.move(oldpath,newpath)
    number += 1
