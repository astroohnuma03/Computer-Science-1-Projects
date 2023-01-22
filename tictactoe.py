#Astro Ohnuma
#11/1/17
#tictactoe.py - first project, tictactoe without graphics
from random import randint
square1 = 1#setting the variables for the different spaces in the board
square2 = 2
square3 = 3
square4 = 4
square5 = 5
square6 = 6
square7 = 7
square8 = 8
square9 = 9
def printboard():#actually creates the board and sets the spaces in the board to be the square variables
    print(' ---','---','---')
    print('|',square1,'|',square2,'|',square3,'|')
    print(' ---','---','---')
    print('|',square4,'|',square5,'|',square6,'|')
    print(' ---','---','---')
    print('|',square7,'|',square8,'|',square9,'|')
    print(' ---','---','---')
def isempty(num1):#checks if a specific space in the board has an X or an O
    if num1 == 1:
        if square1 == 'X' or square1 == 'O':
            return False
        else:
            return True
    elif num1 == 2:
        if square2 == 'X' or square2 == 'O':
            return False
        else:
            return True
    elif num1 == 3:
        if square3 == 'X' or square3 == 'O':
            return False
        else:
            return True
    elif num1 == 4:
        if square4 == 'X' or square4 == 'O':
            return False
        else:
            return True
    elif num1 == 5:
        if square5 == 'X' or square5 == 'O':
            return False
        else:
            return True
    elif num1 == 6:
        if square6 == 'X' or square6 == 'O':
            return False
        else:
            return True
    elif num1 == 7:
        if square7 == 'X' or square7 == 'O':
            return False
        else:
            return True
    elif num1 == 8:
        if square8 == 'X' or square8 == 'O':
            return False
        else:
            return True
    elif num1 == 9:
        if square9 == 'X' or square9 == 'O':
            return False
        else:
            return True
def winner():#checks if someone won the game
    if square1 == square2 and square3 == square2:
        return True
    elif square4 == square5 and square6 == square5:
        return True
    elif square7 == square8 and square9 == square8:
        return True
    elif square1 == square5 and square9 == square5:
        return True
    elif square3 == square5 and square7 == square5:
        return True
    elif square1 == square4 and square7 == square4:
        return True
    elif square2 == square5 and square8 == square5:
        return True
    elif square3 == square6 and square9 == square6:
        return True
    else:
        return False
def fullboard():#checks if the board is full and noone won
    if isempty(1) == False and isempty(2) == False and isempty(3) == False and isempty(4) == False and isempty(5) == False and isempty(6) == False and isempty(7) == False and isempty(8) == False and isempty(9) == False:
        return True
    else:
        return False
if __name__ == '__main__':#makes the program work
    printboard()#calling the function to print the board
    while winner() == False:#checking if someone won the game, if not, starts the first turn or begins another turn
        turn = int(input('Where would you like to go?: '))#asks where the player would like to put their X
        while isempty(turn) == False:#checks if the space the player chose is empty, if it is, asks the player for another space
            turn = int(input('Where would you like to go?: '))
        if turn == 1:#checks if the player chose to place an X on space 1, checks if it is empty, sets the space to an X, reprints the board, checks if the move made the player win, checks if the move made the board full
            isempty(turn)
            square1 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 2:
            isempty(turn)
            square2 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 3:
            isempty(turn)
            square3 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 4:
            isempty(turn)
            square4 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 5:
            isempty(turn)
            square5 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 6:
            isempty(turn)
            square6 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 7:
            isempty(turn)
            square7 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 8:
            isempty(turn)
            square8 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif turn == 9:
            isempty(turn)
            square9 = 'X'
            printboard()
            winner()
            if winner() == True:
                print('Player Wins! Nice Job!')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        com = randint(1,9)#chooses a random space for the computer to place an O
        while isempty(com) == False:#checks if the space is full and if it is, chooses a new random space
            com = randint(1,9)
        if com == 1:
            isempty(com)
            square1 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 2:
            isempty(com)
            square2 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 3:
            isempty(com)
            square3 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 4:
            isempty(com)
            square4 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 5:
            isempty(com)
            square5 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 6:
            isempty(com)
            square6 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 7:
            isempty(com)
            square7 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 8:
            isempty(com)
            square8 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        elif com == 9:
            isempty(com)
            square9 = 'O'
            printboard()
            winner()
            if winner() == True:
                print('Com Wins! Too Bad..')
                break
            fullboard()
            if fullboard() == True:
                print('Full board! Nobody wins!')
                break
        
    