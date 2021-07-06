import random

playerName = input('What is your name?')

highNumber = int(input("{}, please enter a high number".format(playerName)))

theAnswer = random.randint(1,highNumber)

theGuess = None

answerFound = False

numberOfGuesses = 0

while answerFound == False:
    theGuess = int(input("Please enter a guess"))
    print("value of the guess is {}".format(theGuess))
    print("the value of the answer is {}".format(theAnswer))
    if(theGuess == theAnswer):
        print("You guessed correctly")
        answerFound = True
        numberOfGuesses += 1
        print("It took {} guesses".format(numberOfGuesses))
    elif(theGuess == 0):
        print("Ending the game")
        break
    else:
        print("Wrong Answer Try Again")



