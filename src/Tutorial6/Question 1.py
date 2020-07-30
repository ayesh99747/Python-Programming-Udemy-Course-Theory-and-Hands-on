# Produce the following output using any appropriate loops.
#
# Output :
#   Enter a number between 1 to 9 : 5
#   1
#   22
#   333
#   4444
#   55555

count = 0

number_entered = int(input("Enter a number between 1 to 9 : "))
if 0 < number_entered < 10:
    while count < number_entered:
        count = count + 1
        for i in range(0, count):
            print(count, end='')
        print()
else:
    print('Number entered is invalid!')
