from boardLogic import board


def winLogic(square, character):
    row = int(square / 3)
    col = square % 3

    if square == 4:
        if board[0][0] == board[2][2] == character or board[0][1] == board[2][1] == character or \
                board[0][2] == board[2][0] == character or board[1][0] == board[1][2] == character:
            return True
    elif square == 1:
        if board[0][0] == board[0][2] == character or board[1][1] == board[2][1] == character:
            return True
    elif square == 3:
        if board[0][0] == board[2][0] == character or board[1][1] == board[1][2] == character:
            return True
    elif square == 5:
        if board[2][2] == board[0][2] == character or board[1][1] == board[1][0] == character:
            return True
    elif square == 7:
        if board[2][2] == board[2][0] == character or board[1][1] == board[0][1] == character:
            return True
    elif square == 0:
        if board[0][1] == board[0][2] == character or board[1][0] == board[2][0] == character or \
                board[1][1] == board[2][2] == character:
            return True
    elif square == 2:
        if board[0][0] == board[0][1] == character or board[1][2] == board[2][2] == character or \
                board[1][1] == board[2][0] == character:
            return True
    elif square == 6:
        if board[0][0] == board[1][0] == character or board[2][1] == board[2][2] == character or \
                board[1][1] == board[0][2] == character:
            return True
    else:
        if board[0][0] == board[1][1] == character or board[1][2] == board[0][2] == character or \
                board[2][1] == board[2][0] == character:
            return True

    return False
