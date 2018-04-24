# FILE: guessing_game.py
# NAME: Displays if user guessed correct number
# AUTHOR: Anthony Gimei
# DATE: 4/24/2018
# PURPOSE: Accepts guest user input and lets them know if they guessed correctly
# Submission confirmation number:

import random
random_low = 1
random_high = 5
guess_is_good = False
continue_playing = False

while True:
    random_number = random.randint(random_low, random_high)
    print(random_number)
    try:
        user_guess = float(input("Guess a number between 1 and 5:\n"))
        for x in range(random_low, random_high):
            if round(user_guess) == random_number:
                print("You won! Number", round(user_guess), "is the winner")
                guess_is_good = True
                break
            else:
                print("Try your luck again.")
                break
        if guess_is_good:
            want_to_continue = input("Do you want to play again?\n")
            if want_to_continue.lower() != "y" or want_to_continue != "yes":
                continue_playing = True
            else:
                break
        if not continue_playing:
            break
    except ValueError:
        print("Please Enter Valid Number only... try again")
