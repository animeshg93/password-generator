from boardLogic import *
from winLogic import *

counter = 0


def playerMove(player):
    square = int(input("Please enter the square number for your move, from 0-8: "))
    populateBoard(square, player)
    if winLogic(square, player):
        print("The player has won!")
        return True


def computerMove(computer):
    square = int(input("Please enter the square number for computer move, from 0-8: "))
    populateBoard(square, computer)
    if winLogic(square, computer):
        print("The computer has won!")
        return True


def playGame(player, computer):
    global counter
    over = False
    while counter < 8 and not over:
        if playerMove(player) or computerMove(computer):
            over = True
        counter += 2

    # calling the computer function for one last move by the computer
    if not over:
        computerMove(computer)


def game():
    player = input("Welcome to Tic Tac Toe. Please choose your input type, 'X' or 'O': ").upper()
    print(f"You have chosen {player}.")
    computer = 'O' if player == 'X' else 'X'

    playGame(player, computer)


game()
