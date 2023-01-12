board = [['-' for x in range(3)] for y in range(3)]


def printBoard():
    print()
    print("\n".join(' | '.join(x for x in row) for row in board))


def populateBoard(square, character):
    row = int(square / 3)
    col = square % 3

    while board[row][col] != '-':
        square = int(
            input("That square is already taken. Please enter a valid square number, from 0-8: "))
        row = int(square / 3)
        col = square % 3

    board[row][col] = character
    printBoard()
