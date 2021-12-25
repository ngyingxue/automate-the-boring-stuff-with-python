'''
Chess Dictionary Validator
In this chapter, we used the dictionary value {'1h': 'bking', '6c':
'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a
chess board. Write a function named isValidChessBoard() that takes a
dictionary argument and returns True or False depending on if the board
is valid.
A valid board will have exactly one black king and exactly one white
king. Each player can only have at most 16 pieces, at most 8 pawns, and
all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t
be on space '9z'. The piece names begin with either a 'w' or 'b' to
represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook',
'queen', or 'king'. This function should detect when a bug has resulted
in an improper chess board.
'''

testboard = {'1h': 'bking',
        '6c': 'wqueen',
        '2g': 'bbishop',
        '5h': 'bqueen',
        '3e': 'wking'}

def isValidChessBoard(board):
    #setting the control parameter
    errorkey = 0

    #all pieces must be on a valid space from '1a' to '8h'
    numbers = ['1','2','3','4','5','6','7','8']
    alphabets = ['a','b','c','d','e','f','g','h']
    validcells = []

    for x in range(len(numbers)):
        for y in range(len(alphabets)):
            validcells.append(numbers[x]+alphabets[y])

    for keys in board:
        if keys not in validcells:
            errorkey +=1

    black = 0
    white = 0

    #each piece name starts with either a 'w' or 'b'
    for value in board.values():
        if value[0] not in ['b','w']:
            errorkey +=1
        if value[0] == 'b':
            black += 1
        if value[0] == 'w':
            white += 1

    #each player can only have at most 16 pieces
    if black > 16 or white> 16:
        errorkey += 1

    #followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'

    validpieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for value in board.values():
        piece = value[1:]
        if piece not in validpieces:
            errorkey += 1

    #at most 8 pawns each, with exactly one black and white king

    wpawn = 0
    bpawn = 0
    wking = 0
    bking = 0

    for value in board.values():
        if value == 'wpawn':
            wpawn += 1
        if value == 'bpawn':
            bpawn += 1
        if value == 'bking':
            bking += 1
        if value == 'wking':
            wking += 1

    if wpawn > 8 or bpawn >8 or bking != 1 or wking != 1:
        errorkey +=1

    if errorkey>=1:
        return False
    else:
        return True

print(isValidChessBoard(testboard))
