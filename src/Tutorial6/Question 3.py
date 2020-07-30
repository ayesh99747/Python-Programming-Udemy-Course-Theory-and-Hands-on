# Produce the following output using any appropriate loops.
#
# Output :
#   Enter a number between 1 to 9 : 5
#   1****
#   12***
#   123**
#   1234*
#   12345

count = 0

number_entered = int(input("Enter a number between 1 to 9 : "))
count_star = number_entered
if 0 < number_entered < 10:
    while count < number_entered:
        count = count + 1
        count2 = 0
        for i in range(0, count):
            count2 = count2 + 1
            print(count2, end='')
        for i in range(1, count_star):
            print('*', end='')
        count_star = count_star - 1
        print()
else:
    print('Number entered is invalid!')
