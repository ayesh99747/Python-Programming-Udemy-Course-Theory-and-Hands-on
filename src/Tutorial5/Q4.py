#   4. Write a program which asks the user how many stars are required and then make it 
#      display that number of stars across the screen.

count = int(input("Please enter the number of stars to display : "))
for i in range(0, count):
    print("*", end=" ")
