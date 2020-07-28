#   d)	Write a program that checks whether a number is even or odd and then displays 
#       the appropriate message. (Hint – use the % operator).

number = int(input("Enter a number : "))
remainder = number%2
if remainder!=0:
    print("Odd")
else:
    print("Even")