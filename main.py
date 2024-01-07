import shutil
import os
import hangman
import numberGame
import reverseString
import tictactoe

def drawScreen():
  os.system("clear")
  myMenu = '''

██╗  ██╗ ██████╗ ███╗   ███╗███████╗██████╗  █████╗  ██████╗ ███████╗    
██║  ██║██╔═══██╗████╗ ████║██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔════╝    
███████║██║   ██║██╔████╔██║█████╗  ██████╔╝███████║██║  ███╗█████╗      
██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔═══╝ ██╔══██║██║   ██║██╔══╝      
██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗██║     ██║  ██║╚██████╔╝███████╗    
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    
                                                                        
  1) Hangman Game
  2) Number Guessing Game 
  3) Reversing Statement App
  4) Tic Tac Toe
  0) Exit
  '''
  # Draw the main menu centered in the terminal
  print(myMenu.center(shutil.get_terminal_size().columns))

# Main Loop
while(True):
  drawScreen()
  # Get the users selection and run the appropriate game
  choice = input(">")
  if(choice.isdigit()):
    if(choice == '1'):
      hangman.startGame()
    elif(choice == '2'):
      numberGame.startGame()
    elif(choice == '3'):
      reverseString.startGame()
    elif (choice == '4'):
      tictactoe.run()
    elif(choice == '0'):
      break
