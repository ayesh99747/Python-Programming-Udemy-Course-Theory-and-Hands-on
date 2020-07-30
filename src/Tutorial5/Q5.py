#   5. Write a program that simulates the rolling of two six-sided dice and then counts 
#      the number of times that the dice generate a double (e.g. both dice shown the same 
#      value). Roll the dice 100 times and then print the number of doubles. Example output., 
#      Out of 100 you rolled 20 doubles

import random

count = 0  # Store the number of times a double was rolled
for i in range(0, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 == dice2:
        count = count + 1

print("out of 100 you rolled", count, "doubles")
