'''
Selective Copy
Write a program that walks through a folder tree and searches for files with a certain
file extension (such as .pdf or .jpg). Copy these files from whatever location they are
in to a new folder.
'''

import os, shutil
from pathlib import Path

source = os.path.abspath(input('Enter a folder path to copy from:\n'))
destination = os.path.abspath(input('Enter a folder path to copy to:\n'))
extension = input('Enter desired extension\n')

for foldername, subfolders, filenames in os.walk(source):
    for filename in filenames:
        if filename.endswith(extension):
            copyPath = os.path.join(foldername, filename)
            print(copyPath)
            shutil.copy(copyPath, destination)
