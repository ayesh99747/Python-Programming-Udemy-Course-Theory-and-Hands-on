# 2. Write a program that uses a for loop to read in 5 numbers and output the total.

total = 0
for i in range(1, 6):
    number_entered = int(input("Please enter a number : "))
    total = total + number_entered
print("The total is :", total)
