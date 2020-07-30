# 8. Exception Handling in Python
#   a) When we think that some commands may fail, we create an exception handler for the errors we expect using the try…except construct.
#       try:
#           Python commands
#       except:
#           Exception handler
#
#   The above construct does not specify a specific exception (error) to handle, so the exception handler is user for any errors that occur while executing the Python commands.
#       try:
#           Python commands
#       except ExceptionType:
#           Exception handle
#
#   If the exception handler only handles certain exceptions (specified in the ExceptionType) 
#   and the program produces an exception that the handler wasn’t written to deal with, 
#   Python’s default exception handler will handle that error.
#
#   In the following example we ask the user to enter an integer number and cast the string 
#   input from the input() method to an integer. If the input entered is not been an integer 
#   and cannot be converted (cast) to an integer it will generate a ValueError.