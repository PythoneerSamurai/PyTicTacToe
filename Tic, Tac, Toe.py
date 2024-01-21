import random

board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
notAllowed = [0] * 9
userChoice = int
compChoice = int
user_isCheck = True
comp_isCheck = True
winCheck = int
p, z, x = 8, 0, 0


def printBoard():
    print("-------------")
    for elements in board:
        for element in elements:
            print('|', element, end=" ")
        print('|')
        print("-------------")


def winChecker():
    global winCheck

    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':

        winCheck = 1

    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':

        winCheck = 1

    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':

        winCheck = 1

    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':

        winCheck = 1

    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':

        winCheck = 1

    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':

        winCheck = 1

    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':

        winCheck = 1

    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':

        winCheck = 1

    elif board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0':

        winCheck = 2

    elif board[1][0] == '0' and board[1][1] == '0' and board[1][2] == '0':

        winCheck = 2

    elif board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0':

        winCheck = 2

    elif board[0][0] == '0' and board[1][0] == '0' and board[2][0] == '0':

        winCheck = 2

    elif board[0][1] == '0' and board[1][1] == '0' and board[2][1] == '0':

        winCheck = 2

    elif board[0][2] == '0' and board[1][2] == '0' and board[2][2] == '0':

        winCheck = 2

    elif board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0':

        winCheck = 2

    elif board[0][2] == '0' and board[1][1] == '0' and board[2][0] == '0':

        winCheck = 2

    else:

        winCheck = 3


def compChoice():
    def comp_notAllowed():

        global comp_isCheck
        for elements in notAllowed:
            if compChoice == elements:
                comp_isCheck = False
                break
            else:
                comp_isCheck = True

    global board
    global notAllowed
    global p

    while 1 == 1:

        if p == 4:

            winChecker()

            if winCheck == 1:

                print("\nYou won!")
                print("\n")
                printBoard()
                print("\n")
                break

            elif winCheck == 2:

                print("You lost the match to the computer!")
                print("\n")
                printBoard()
                print("\n")
                break

            else:

                print("\nThe game ended at a draw!")
                print("\n")
                printBoard()
                print("\n")
                break

        else:

            compChoice = random.randint(1, 9)
            comp_notAllowed()

            if comp_isCheck == True:

                if compChoice == 1:

                    board[0][0] = '0'
                    notAllowed[p] = compChoice
                    print("\n")
                    printBoard()
                    print("\n")

                elif compChoice == 2:

                    board[0][1] = '0'
                    notAllowed[p] = compChoice
                    print("\n")
                    printBoard()
                    print("\n")

                elif compChoice == 3:

                    board[0][2] = '0'
                    notAllowed[p] = compChoice
                    print("\n")
                    printBoard()
                    print("\n")

                elif compChoice == 4:

                    board[1][0] = '0'
                    notAllowed[p] = compChoice
                    print("\n")
                    printBoard()
                    print("\n")

                elif compChoice == 5:

                    board[1][1] = '0'
                    notAllowed[p] = compChoice
                    print("\n")
                    printBoard()
                    print("\n")

                elif compChoice == 6:

                    board[1][2] = '0'
                    notAllowed[p] = compChoice
                    print("\n")
                    printBoard()
                    print("\n")

                elif compChoice == 7:

                    board[2][0] = '0'
                    notAllowed[p] = compChoice
                    print("\n")
                    printBoard()
                    print("\n")

                elif compChoice == 8:

                    board[2][1] = '0'
                    notAllowed[p] = compChoice
                    print("\n")
                    printBoard()
                    print("\n")

                else:

                    board[2][2] = '0'
                    notAllowed[p] = compChoice
                    print("\n")
                    printBoard()
                    print("\n")

                p -= 1
                break

            else:
                continue


def userChoice():
    global userChoice
    global board
    global notAllowed
    global z
    global x

    def user_notAllowed():

        global user_isCheck
        for elements in notAllowed:
            if userChoice == elements:
                user_isCheck = False
                break
            else:
                user_isCheck = True

    while x < 5:

        winChecker()

        if winCheck == 1:

            print("You won!\n")
            break

        elif winCheck == 2:

            print("\nYou lost the match to the computer!")
            break

        else:

            try:

                userChoice = int(input("Enter a position from 1 to 9, where you want to place a 'X': "))
                user_notAllowed()

                if user_isCheck == True:

                    if userChoice == 1:

                        board[0][0] = 'X'
                        notAllowed[z] = userChoice
                        x += 1
                        z += 1
                        compChoice()

                    elif userChoice == 2:

                        board[0][1] = 'X'
                        notAllowed[z] = userChoice
                        x += 1
                        z += 1
                        compChoice()

                    elif userChoice == 3:

                        board[0][2] = 'X'
                        notAllowed[z] = userChoice
                        x += 1
                        z += 1
                        compChoice()

                    elif userChoice == 4:

                        board[1][0] = 'X'
                        notAllowed[z] = userChoice
                        x += 1
                        z += 1
                        compChoice()

                    elif userChoice == 5:

                        board[1][1] = 'X'
                        notAllowed[z] = userChoice
                        x += 1
                        z += 1
                        compChoice()

                    elif userChoice == 6:

                        board[1][2] = 'X'
                        notAllowed[z] = userChoice
                        x += 1
                        z += 1
                        compChoice()

                    elif userChoice == 7:

                        board[2][0] = 'X'
                        notAllowed[z] = userChoice
                        x += 1
                        z += 1
                        compChoice()

                    elif userChoice == 8:

                        board[2][1] = 'X'
                        notAllowed[z] = userChoice
                        x += 1
                        z += 1
                        compChoice()

                    elif userChoice == 9:

                        board[2][2] = 'X'
                        notAllowed[z] = userChoice
                        x += 1
                        z += 1
                        compChoice()

                    else:
                        print("Invalid position entered, re-enter the position.\n")
                        continue

                else:
                    print("The position that you entered is already occupied. Choose another position.\n")
                    continue

            except ValueError:
                print("You did not choose any position. Enter a position below.\n")
                continue


print("The game has begun!\n")
printBoard()
print("\n")
userChoice()
