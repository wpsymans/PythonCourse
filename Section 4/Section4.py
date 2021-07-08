#this does a few things including while loop and if, elif and else
import random
numberOfTries = 0
highest = 10
name = input("please enter your name")
theNumber = random.randint(1,highest)
answerFound = False
quitImDone = False

while answerFound == False & quitImDone == False:
    guess = int(input("Enter a guess between 1 and {}".format(highest)))

    if guess == theNumber:
        print("You found the right number!")
        print("You got the right answer in {}".format(numberOfTries +1))
        answerFound = True
        quitImDone = True
    elif guess > theNumber:
        print("too high")
        numberOfTries = numberOfTries + 1
    else:
        print("Too Low")
        numberOfTries = numberOfTries + 1