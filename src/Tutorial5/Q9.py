# 9. Test what type of error the following will produce.
#   >>> x = 2/0
#   • Then create a try except construct that will give the message ‘Cannot divide by zero’ 
#     when appropriate.

number_entered = int(input('Please enter the divisor : '))
try:
    x = 2 / number_entered
    print('The answer is :', x)
except ZeroDivisionError:
    print('Cannot divide by zero')
