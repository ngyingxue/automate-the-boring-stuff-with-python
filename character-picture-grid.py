'''
Character Picture Grid
Say you have a list of lists where each value in the inner lists is a one-character string, like this:
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
Think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text
characters. The (0, 0) origin is in the upper-left corner, the x-coordinates increase going right, and the ycoordinates increase going down.
Copy the previous grid value, and write code that uses it to print the image.
'''

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

rows = len(grid)
cols = len(grid[0])

for j in range(cols):
    for i in range(rows):
        print(grid[i][j], end=' ')
    print()
