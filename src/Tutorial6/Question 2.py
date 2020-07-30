# Produce the following output using any appropriate loops.
#
# Output :
#   Enter a number between 1 to 9 : 5
#       1
#      1 2
#     1 2 3
#    1 2 3 4
#   1 2 3 4 5

count_1 = 0

num = int(input("Please Enter a Number between 1 to 9 : "))
if 1 <= num <= 9:  # This line verifies if the number is within 1 and 9
    count_2 = num
    while count_1 < num:
        count_3 = 0  # count_3 is the count for the number that is to be printed
        count_1 = count_1 + 1
        for i in range(count_2, 1, -1):  # This for loop is for the number of spaces to be printed
            print(" ", end="")
        for i in range(0, count_1):  # This for loop is for the numbers to be printed
            count_3 = count_3 + 1
            print(count_3, end=" ")
        print()
        count_2 = count_2 - 1
    count_2 = num - 1
else:
    print("Number is invalid")
