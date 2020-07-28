#   3.	Python has a random module that provides pre-written functions to generate random 
#       numbers. To use the functions in the random module use the import statement at the 
#       top of your code:
#               import random

#       Then randint function will return a random integer between (and including) the two integer arguments you pass it. We will store this random number in the variable called secret_number.
#               secret_number = random.randint(1,20)

#       To access the randint function we prefix it with the name of the module imported.
#       You can also try different ranges of numbers by changing the arguments. For example:
#               random.randint(1, 4)	# integers between 1 and 4 (including both 1 and 4).

#   a)	Write a program that simulates a single flip of a coin. It should randomly 
#       print either ‘Heads’ or ‘Tails’. Hint: generate a random number (0 or 1) and 
#       use an if-else statement to print ‘Heads’ when the result is 0, or ‘Tails’ otherwise.

import random

random_number = random.randint(0,1)
if random_number == 0:
    print('Heads')
else:
    print('Tails')