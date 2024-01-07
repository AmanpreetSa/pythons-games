import os

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#function prints the game board. Each individual print statement for the rows are used four times, and the columns seperated are used three times. 
def drawBoard():
    os.system("clear")
    print("*---*---*---*")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("*---*---*---*")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("*---*---*---*")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("*---*---*---*")

#asks the player to enter their move on the board by picking a number from 1-9. It updates the board by whatever the player enters. But it will also tell the player if a spot on the board is taken by checking to see if there is a icon already there. Checks a single spot if the spot is taken by checking if there is a number. -1 makes sure to select the right index is chosen since lists start at 0 
def playersTurn(icon):
  print(f"Your turn player {icon}")
  while True:
    choice = int(input("Enter your move (1-9): "))
    if board[choice - 1].isdigit():
        board[choice - 1] = icon
        break
    else:
        print("\nThat space is taken!")

#checks each position on the board to see if there is a tile, and then returns True or False depending if someone ended up getting three in a row. 
def checkIfWinner(tile):
    # checks horizontal
    if board[0] == board[1] == board[2] == tile:
        return True
    elif board[3] == board[4] == board[5] == tile:
        return True
    elif board[6] == board[7] == board[8] == tile:
        return True
        
    # checks vertical
    elif board[0] == board[3] == board[6] == tile:
        return True
    elif board[1] == board[4] == board[7] == tile:
        return True
    elif board[2] == board[5] == board[8] == tile:
        return True

    # checks diagonal
    elif board[0] == board[4] == board[8] == tile:
        return True
    elif board[2] == board[4] == board[6] == tile:
        return True
    
    return False

#the isdigit function checks to see if there any numbers on the board remaining. If there are numbers, that mean the game is still running and there are spots to still be chosen. However, if there are no numbers left, and the winner was checked by the previous function, that means it is a tie. 
def isTie():
    for spot in board:
        if spot.isdigit():
            return False
    return True

#asks the user if they want to play again by typing "y" for yes and "n" for no
def playAgain():
    choice = input("Play again? (y/n): ")
    if choice.lower() == "y":
        return True
    else:
        return False

def run():
    global board
    os.system("clear")
    while True: 
        #prints the board
        drawBoard()
        #X enters their move on the board
        playersTurn("X")
        #checks if X won 
        if checkIfWinner("X"):
            #updates the board 
            drawBoard()
            print("X wins! Congratulations!")
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            #asks the user to play again, and then breaks if they decline
            if playAgain():
                continue
            else:
                break
        #checks for tie
        elif isTie():
            drawBoard()
            print("It's a draw!")
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            #asks to play again since it's a tie which is a different outcome 
            if playAgain():
                continue
            else:
                break
        drawBoard()
        #O enters their move on the board
        playersTurn("O")
        #checks if O won 
        if checkIfWinner("O"):
            #updates board
            drawBoard()
            print("O wins! Congratulations!")
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            #asks to play again 
            if playAgain():
                continue
            else:
                break
        #checks if there is a tie 
        elif isTie():
            #updates board
            drawBoard()
            print("It's a draw!")
            # ask the user to play again
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            #asks to play again
            if playAgain():
                continue
            else:
                break
            
