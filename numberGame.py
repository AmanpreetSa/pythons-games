import random
import os

#function asks the user for a guess, the variable holds it, and makes it a integer
def userGuess():
  myGuess = input("Please enter a number: ")
  if not myGuess.isdigit():
    print("You may only enter a number")
    return userGuess()
  return int(myGuess)

#function asks the user if they would like to play the game again, holds that reponse in a variable called playback which checks if the response was 'yes', and runs the start game function and clears the screen or otherwise stops the game 
def resetGame():
  playback = input("Would you like to play again? ")
  if playback == "yes":
    os.system('clear')
    startGame()
  else:
    return False

#function gets a random number and the variable holds it, and then the if statements check to see if the user ends up having a number higher or lower and adds a try to the tries variable till the user enters the correct number wher eit will stop checking 
def startGame():
  os.system('clear')
  possibleNumbers = random.randint(1, 100)
  tries = 0
  while True:
    myGuess = userGuess()

    os.system("clear")

    if myGuess == possibleNumbers:
      print("You took", tries , "tries to guess the number!")
      if resetGame() == False:
        break
    elif myGuess > possibleNumbers:
      print("The guess is higher than the number")
      tries += 1
    elif myGuess < possibleNumbers:
      print("The guess is lower than the number")
      tries +=1
