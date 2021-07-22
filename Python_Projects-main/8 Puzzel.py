# Implementation of One Player 8  puzzel game in Python.
# By: Darpit Makwana

# Goal State
goalBoard = {1: '1', 2: '2', 3: '3',
             4: '4', 5: '5', 6: '6',
             7: '7', 8: '8', 9: ' '}

# Initial State
initialBoard = {1: '1', 2: '2', 3: '3',
                4: '4', 5: ' ', 6: '6',
                7: '7', 8: '5', 9: '8'}

# Printing The Board
def printBoard(board):
    """This Function print Full Game Bard."""
    print(' | ' +board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
    print(' | ' +board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    print(' | ' +board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')

# Main Game Function
def game():

    # Check Position of ' ' In Initial Board
    for i in range(1, 10):
        if initialBoard[i] == ' ':
            space = i
            print(space)
            break

    print("=====Your Goal=====")
    printBoard(goalBoard)
    print("\n=====Let's Strt Game Now=====")
    printBoard(initialBoard)

    # Run Loop For 50 Times With Wrong or Correct Inputs
    for i in range(50):
        if space == 4 or space == 5 or space == 6 or space == 7 or space == 8 or space == 9:
            print("W = Up")
        if space == 1 or space == 2 or space == 3 or space == 4 or space == 5 or space == 6:
            print("S = Down")
        if space == 2 or space == 3 or space == 5 or space == 6 or space == 8 or space == 9:
            print("A = Left")
        if space == 1 or space == 2 or space == 4 or space == 5 or space == 7 or space == 8:
            print("D = Right")

        move = input("\nEnter Your Move :")

        # Move Perform according to w,s,a,d
        if (move=='w' or move=='w') and (space == 4 or space == 5 or space == 6 or space == 7 or space == 8 or space == 9):
            initialBoard[space] = initialBoard[space - 3]
            initialBoard[space - 3] = ' '
            space-=3
            # Check Winning Condition
            if initialBoard==goalBoard:
                printBoard(initialBoard)
                print("\n====Congratulations, You AChive Goal====")
                break
            printBoard(initialBoard)

        elif (move=='S' or move=='s') and (space == 1 or space == 2 or space == 3 or space == 4 or space == 5 or space == 6):
            initialBoard[space] = initialBoard[space + 3]
            initialBoard[space + 3] = ' '
            space+=3
            if initialBoard==goalBoard:
                printBoard(initialBoard)
                print("\n====Congratulations, You AChive Goal====")
                break
            printBoard(initialBoard)

        elif (move=='A' or move=='a') and (space == 2 or space == 3 or space == 5 or space == 6 or space == 8 or space == 9):
            initialBoard[space] = initialBoard[space - 1]
            initialBoard[space - 1] = ' '
            space-=1
            if initialBoard==goalBoard:
                printBoard(initialBoard)
                print("\n====Congratulations, You AChive Goal====")
                break
            printBoard(initialBoard)

        elif (move=='D' or move=='d') and (space == 1 or space == 2 or space == 4 or space == 5 or space == 7 or space == 8):
            initialBoard[space] = initialBoard[space + 1]
            initialBoard[space + 1] = ' '
            space+=1
            if initialBoard==goalBoard:
                printBoard(initialBoard)
                print("\n====Congratulations, You AChive Goal====")
                break
            printBoard(initialBoard)
        else :
            print("\nInvalid Input. Try Again...")
            continue

#Run Game Code
game()
