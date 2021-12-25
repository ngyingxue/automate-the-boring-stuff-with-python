'''
Table Printer
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table
with each column right-justified. Assume that all the inner lists will contain the same number of strings. 

Hint: your code will first have to find the longest string in each of the inner lists so that the whole column
can be wide enough to fit all the strings. You can store the maximum width of each column as a list of
integers. The printTable() function can begin with colWidths = [0] * len(tableData), which will create a list
containing the same number of 0 values as the number of inner lists in tableData. That way, colWidths[0] can
store the width of the longest string in tableData[0], colWidths[1] can store the width of the longest string in
tableData[1], and so on. You can then find the largest value in the colWidths list to find out what integer width
to pass to the rjust() string method.
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    for y in range(len(table)):
        for x in table[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)
    for x in range(len(table[y])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidths[y]+1), end ='')
        print()

printTable(tableData)
