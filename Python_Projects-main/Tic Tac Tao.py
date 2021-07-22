# Implementation Of Two Player Tic-Tac-Toe Game In Python.
# By : Darpit Makwana

# Initialize dictionary for board. Which have initially empty/null value.
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

# Initialize Dictionary For Both Player's Name
playerName = {'X':' ','O':' '}

def printBoard(board):
    """This Function print Full Game Bard."""
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0

    # Get Both Player Name
    playerName["X"] = input("Enter First player Name : ")
    print(playerName["X"],"Your Sign is X.\n")
    playerName["O"] = input("Enter Second player Nname : ")
    print(playerName["O"], "Your Sign is O.\n")

    print("=====Let's Strt Game Now=====")

    for i in range(30):
        print()
        printBoard(theBoard)
        move = input(playerName[turn] + " it's your turn. Move to which place? : ")

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nPlease Try Another Place.")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                print()
                printBoard(theBoard)
                print("\n===== GAME OVER =====")
                print(" **** " + playerName[turn] + " Win The Game. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                print()
                printBoard(theBoard)
                print("\n===== GAME OVER =====")
                print(" **** " + playerName[turn] + " Win The Game. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                print()
                printBoard(theBoard)
                print("\n===== GAME OVER =====")
                print(" **** " + playerName[turn] + " Win The Game. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                print()
                printBoard(theBoard)
                print("\n===== GAME OVER =====")
                print(" **** " + playerName[turn] + " Win The Game. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                print()
                printBoard(theBoard)
                print("\n===== GAME OVER =====")
                print(" **** " + playerName[turn] + " Win The Game. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                print()
                printBoard(theBoard)
                print("\n===== GAME OVER =====")
                print(" **** " + playerName[turn] + " Win The Game. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                print()
                printBoard(theBoard)
                print("\n===== GAME OVER =====")
                print(" **** " + playerName[turn] + " Win The Game. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                print()
                printBoard(theBoard)
                print("\n===== GAME OVER =====")
                print(" **** " + playerName[turn] + " Win The Game. ****")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print()
            printBoard(theBoard)
            print("\n===== GAME OVER =====")
            print("It's a Tie!!")
            break

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.
    restart = input("\nDo want to play Again?(Y/N) : ")
    if restart == "y" or restart == "Y":
        for key in theBoard:
            theBoard[key] = " "
        print("===================================\n")

        game()

# Execute game function
if __name__ == "__main__":
    game()