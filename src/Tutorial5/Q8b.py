# b) For example, in the following the user enters 10.5 instead of a valid integer.
#   
#   >>> n = int(input("Please enter a number: "))
#   Please enter a number: 10.5
#   Traceback (most recent call last):
#       File "<stdin>", line 1, in <module>
#   ValueError: invalid literal for int() with base 10: '10.5'
#
#   With the aid of exception handling, we can write robust code for reading an integer 
#   from input:
#       n = input("Please enter an integer: ")
#       try:
#           n = int(n)
#       except ValueError:
#           print("Requires a valid integer!")
#
#   Example: The program accepts a value from the user. In the try clause the value in n is 
#   converted (cast) to an integer. If an exception occurs (the value cannot be converted 
#   to an integer) the except clause will be executed. The error, in this case a ValueError, 
#   has to match the name after except.