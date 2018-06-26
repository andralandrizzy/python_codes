import random

def main():
    username = str(input("Please Enter Your Name: "))
    print('Welcome' + username)
    question = str(input("Would you like to play a guessing game," + username + "? [Y/N] "))
    if question == 'y':
        print("Great Let's begin! ")
    if question == 'n':
        print("Ohh...okay bye!")

main()