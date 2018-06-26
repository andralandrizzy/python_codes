# Author: Andral Orelus
# Date: December 23, 2017
# Description: Guesing game.

import random

print("Welcome to the guessing game!")
randomNumber = random.randint(1, 50)
def main():
    userName = str(input("Please your name: "))
    print("Thanks the name was successfully entered")
    questions = str(input(userName, " Would you like to play a guessing game? [Y/N]"))
    if questions == 'n':
        print("ohhh okay bye!")
    if questions == 'y':
        print("I am thinking of a number between 1 to 50. Can you guess it?")
    found = False

    while not found:
        userGuess = int(input("Your guess: "))
        if userGuess == randomNumber:
            print("Good job ",userName," You got it!")
            found = True
        elif userGuess > randomNumber:
            print("Nope. Guess lower!")
        else:
            print("Nope. Guess higher!")
    print("Bye and Thank you for playing our guessing game.")

if __name__ == "__main__":
    main()

    