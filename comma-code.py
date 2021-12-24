'''
Comma Code
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string with all the items separated by
a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the
function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any
list value passed to it. Be sure to test the case where an empty list [] is passed to your function.
'''

#spam = ['apples', 'bananas', 'tofu', 'cats']

#spam = ['apples']

def comma(myList):
    value = ' '
    if len(myList) == 1:
        print(myList[0])
    if len(myList)>1:
        for i in range(len(myList)):
            if i == len(myList)-1:
                value += 'and '+ myList[i]
            else:
                value += myList[i] + ', '
        print(value)

comma(spam)
