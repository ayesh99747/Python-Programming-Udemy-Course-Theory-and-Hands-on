# Exercise 2 - Guess the number program (limit number of guesses)
#   • The solution for exercise 2 should only allow a maximum of 5 guesses. If a correct 
#     guess is entered then use a break to exit the while loop.
#       o Write a program that picks a random number between 1 and 20 and allows the user 
#         a maximum of five attempts to guess the number.
#       o For each incorrect guess, the program will let the user know if the correct answer 
#         is higher or lower than the user’s guess.
#   a) If the user doesn’t guess the answer in five attempts, the loop will end and the 
#      program will tell the user what the number was.
#   b) If the user guesses the answer within 5 attempts, the program will break from the 
#      loop and tell the user they are correct and how many guesses it took.
#       o You will need to add a check directly after the loop to decide which message 
#         is appropriate. E.g., either a) or b) above.

import random

hidden = random.randint(1, 20)
count = 0
entered_num = 0
while count < 5 and entered_num != hidden:
    entered_num = int(input("Guess the number(Between 1 & 20)"))
    if entered_num != hidden:
        if entered_num > hidden:
            print("Entered value was too high!")
        elif entered_num < hidden:
            print("Entered value was too low!")
        print("Please guess again: ")
        count = count + 1
    else:
        print("Your guess was correct!")
if count < 5:
    print("You were able to guess the correct answer in: ", count+1, 'attempts')
else:
    print("You have run out of attempts")
    print("The correct answer is: ", hidden)