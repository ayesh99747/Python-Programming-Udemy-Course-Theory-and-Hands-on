#   1. Write a program to print the times table for a number entered by the user. 
#
#     Example Output:
#       Enter the number to print the tables for: 7
#       7 x 1 = 7
#       7 x 2 = 14
#       7 x 3 = 21
#       7 x 4 = 28
#       7 x 5 = 35
#       7 x 6 = 42
#       7 x 7 = 49
#       7 x 8 = 56
#       7 x 9 = 63
#       7 x 10 = 70

count = 0
number_entered = int(input("Enter the number to print the tables for: "))
for i in range(1, 11):
    count = count + 1
    answer = number_entered * count
    print(number_entered, " x ", count, " = ", answer)
