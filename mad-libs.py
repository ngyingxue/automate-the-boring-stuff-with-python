import re

madLibs = open('madLibs.txt', 'r')
newMadLibs = open('newMadLibs.txt', 'w')

text=madLibs.read()

print(text)

textList = re.findall(r'\w+|[^\w\s]', text)
#\w+ -> 1 or more word character (alphanumeric)
#| -> or
#[^\w\s] -> exclude alphanumeric or space

newList=[]

for i in textList:
    if i == 'ADJECTIVE':
        i = input('Enter an adjective:\n')
        newList.append(i)
    elif i == 'NOUN':
        i = input('Enter a noun:\n')
        newList.append(i)
    elif i == 'ADVERB':
        i = input('Enter an adverb:\n')
        newList.append(i)
    elif i == 'VERB':
        i = input('Enter a verb:\n')
        newList.append(i)
    else:
        newList.append(i)

joinText = ' '.join(newList)

newText = re.sub(r'\s([^\w\s])', r'\1',joinText)

print(newText)

newMadLibs.write(newText)

madLibs.close()
newMadLibs.close()
