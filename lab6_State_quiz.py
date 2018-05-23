# FILE: lab_6_State_quiz.py
# NAME: Displays state abbreviation for user to guess
# AUTHOR: Anthony Gimei
# DATE: 5/23/2018
# PURPOSE: Accepts user guess of displayed State abbreviation and lets user know how many the got correct

import random
random_low = 1
random_high = 5
continue_playing = True

while continue_playing:
    random_number = random.randint(random_low, random_high)
    try:
        user_guess = float(input("Guess a number between 1 and 5:\n"))
        if round(user_guess) == random_number:
            print("You won! Number", round(user_guess), "is the winner")
            want_to_continue = input("Do you want to play again(Type 'y' or 'yes' to play again)?\n")
            if want_to_continue.lower() == "y" or want_to_continue == "yes":
                continue_playing = True
            else:
                continue_playing = False
        else:
            print("You've guessed the wrong number.\nTry your luck again.\n")
    except ValueError:
        print("Please Enter Valid Number only... try again")
