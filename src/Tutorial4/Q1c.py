# Part C - 
#   Amend the program to let the user know if each guess is correct, too low or too 
#   high. Use an if, elif, else.

import random

hidden = random.randint(1, 20)
entered_num = int(input("Guess the number(Between 1 & 20)"))
if entered_num == hidden:
    print("Your guess was correct!")
else:
    while entered_num != hidden:
        if entered_num > hidden:
            print("Entered value was too high!")
        elif entered_num < hidden:
            print("Entered value was too low!")
        print("Please guess again: ")
        entered_num = int(input("Guess the number(Between 1 & 20)"))
    print("Your guess was correct!")