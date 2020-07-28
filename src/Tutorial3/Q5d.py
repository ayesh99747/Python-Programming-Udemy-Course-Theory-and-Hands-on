#   d)	Test the code given below.

#       if mark >= 70:
#           print(’Exceptional result!’)
#       elif mark >= 40:
#           print(’Satisfactory result!’)
#       else:
#           print(’You have failed.’)

#   •	Add an additional condition at the start of the program to check if the exam 
#       mark is invalid (less than 0 or greater than 100):

#       if mark < 0 or mark > 100: 
#           print(‘Invalid mark’)

#   •	Trace which line would be printed for the following marks?
#           -0,	0, 1	    69,	70, 71
#           39,	40, 41	    99,	100, 101

mark=101
if mark<0 or mark>100:
    print('Invalid Mark')
else:
    if mark>=70:
        print('Exceptional result!')
    elif mark>=40:
        print('Satisfactory result!')
    else:
        print('You have failed')