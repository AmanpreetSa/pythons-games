import os

def reverse_string(string):
    string = string.split()    #splits the string into a list
    for i in range(len(string)):    #loops over the string 
        string[i] = string[i][::-1] #reverses letters in the words/sentence which the for looped checked
    return ' '.join(string) 

def resetGame():
  playback = input("Would you like to play again? ")
  if playback == "yes":
    os.system('clear')
    startGame()
  else:
    return False

def startGame():
  string = input("Enter a string: ")    #tells you to input a string
  print(reverse_string(string)) #prints the string with the words flipped
  resetGame()
