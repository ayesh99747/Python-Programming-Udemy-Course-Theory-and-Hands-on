# Exercise 3
#   • Write a program that will allow a user to enter a number of scores until -9 is entered.
#   • When -9 is entered, print the average of the scores entered. Use a while loop.
#   • Ensure that at least one score has been entered before calculating the average 
#     (division by zero would produce an error).

total = 0
count = 0
entered_num = 0
while entered_num != -9:
    entered_num = int(input("Please enter a number : "))
    if entered_num != -9:
        total = total + entered_num
        count = count + 1

if count != 0:
    average = total / count
    print(average)
else:
    print("No values were entered!")