import os
import time
import random 

#all the sprites for the hangman game is in this list
totalSprites = [
'''

------╋          
      |
      |
      |
      |
      |
      |
========
'''
,
                
'''

------╋          
  O   |
      |
      |
      |
      |
      |
========
'''         
,
'''

------╋          
  O   |
  |   |
      |
      |
      |
      |
========
'''
,
'''

------╋          
  O   |
  |-- |
      |
      |
      |
      |
========
'''

,
'''

------╋          
  O   |
--|-- |
      |
      |
      |
      |
========
'''
,
'''

------╋          
  O   |
--|-- |
 /    |
      |
      |
      |
========
'''
,

  '''

------╋          
  O   |
--|-- |
 / \  |    GAME OVER :(
      |
      |
      |
========

'''

]

#start from 0 to the length of the list, but then substract 1 because len starts at 1
def getRandomWord() -> str:
  return randomWords[random.randint(0, len(randomWords) - 1)]

#contains number of failures the user has done throughout the game
failures = 0
#the list contains all the words that can be chosen to play the hangman game 
randomWords = ['KEYBOARD', 'BEAN', 'MACHINE', 'SCRIBBLE', 'IRON', 'BASKETBALL', 'CHAIR', 'DESK', 'SHIRT']
myWord = getRandomWord()
myGuesses = []
hasWon = False

def isLetterInWord(letter: str, word: str)-> bool:
  '''
  returns a true statement if the given letter is in the word
  '''
  isInWord = False
  for x in word: 
    if x == letter:
      isInWord = True
      break
  return isInWord

def drawScreen():
  '''
  this function draws the current game screen
  '''
  os.system("clear")
  #displays the current hangman sprite
  print(totalSprites[failures])
  #prints out the word with any guessed letters filled in and any remaining letters as an underscore
  isFound = False
  displayString = ""
  global hasWon
  hasWon = True
  for i in myWord:
    for j in myGuesses:
      if(i==j):
        #checks if letter is found, then it breaks since there is not need to continue
        isFound = True 
        break
    if (isFound):
      displayString += i 
    else:
      displayString += "_"
      hasWon = False
    isFound = False
  print(displayString)
  
  print("\nMy guesses are:\n", myGuesses)

def resetGame():
  playback = input("Would you like to play again? ")
  if playback == "yes":
    os.system('clear')
    startGame()
  else:
    return False

def run():
  global failures
  while (True):
    #this gets a letter from the user
    myGuess = input("Enter your guess: ")
    #confirms that the input is a letter
    if(myGuess.isalpha()):
      #converts it to uppercase
      myGuess = myGuess.upper()
      #is the letter in the word 
      if(not isLetterInWord(myGuess, myWord)):
        #increments failures 
        failures += 1
      #adds the letter to the guess list 
      isFound = False 
      for i in myGuesses:
        if (i == myGuess):
          isFound = True 
          break
      if(not isFound):
        myGuesses.append(myGuess)
    else:
      print("Please enter a letter!")
    #this checks if the user has won
    print(hasWon)
    if(hasWon):
      print("CONGRATULATIONS YOU WON")
      if resetGame() == False:
        break
    elif(failures >= len(totalSprites)-1):
      print("YOU LOST, the word was", myWord + "!")
      if resetGame() == False:
        break
  
    drawScreen()
    
def startGame():
  global myWord
  global hasWon
  global myGuesses
  global failures
  myWord = getRandomWord()
  hasWon = False
  myGuesses = []
  failures = 0
  os.system('clear')
  run()
