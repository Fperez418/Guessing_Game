"""
Guessing Game. The program will do the following:
1. Generate random number between 1 and 9 (including 1 and 9)
2. Prompt user for a guess input
3. Let the user know if they are too high or too low
4. Let the user guess until they've figured it out - print number of guesses
5. Ask user to start new game or exit
"""


from time import sleep
from random import randint

# GENERATES RANDOM NUMBER FOR USER TO GUESS


def generate_number():
    number = randint(1, 9)
    return number

# TAKES USER INPUT/GUESS AND COMPARES IT TO THE RANDOMLY GENERATED NUMBER


def user_guess(number):
    guesses = 0
    turns = True
    while turns is True:
        user_input = int(raw_input("Enter a guess betweein 1 and 9: "))
        if user_input < 1 or user_input > 9:
            print "Calculating..."
            sleep(1)
            print "\nError, invalid input."
            guesses += 1
        elif user_input > number:
            print "Calculating..."
            sleep(1)
            print "\nYour guess is too high, try lower."
            guesses += 1
        elif user_input < number:
            print "Calculating..."
            sleep(1)
            print "\nYour guess is too low, try higher."
            guesses += 1
        elif user_input == number:
            print "Calculating..."
            sleep(1)
            print "\nCongratulations! You guessed correctly!"
            guesses += 1
            if guesses > 1:
                print "\nIt took you %d tries." % guesses
                turns = False
            else:
                print "\nIt only took you %d try!" % guesses
                turns = False

# MANAGES TURNS - ALLOWS USER TO START NEW GAME OR EXIT


def game_manager():
    print "Hello! Welcome to the Guessing Game. In this game, the computer will think of a number between 1 and 9 - it's your job to guess the right number in as few guesses as possible.."
    menu = raw_input("\nEnter 'S' to start a new game or 'X' to exit: ")
    menu = menu.lower()
    game_on = True
    while game_on is True:
        if menu == "s":
            print "..."
            sleep(1)
            print ".."
            sleep(1)
            print "."
            sleep(1)
            user_guess(generate_number())
            option = raw_input("Enter 'S' to start a new game or 'X' to exit: ")
            option = option.lower()
            if option == "s":
                game_on = True
            elif option == "x":
                game_on = False
        elif menu == "x":
            game_on = False

game_manager()
