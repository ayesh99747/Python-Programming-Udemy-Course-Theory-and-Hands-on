#   b)	Write a program to read in someone’ age. Display ‘can vote’ if they are old enough.

age = int(input("Please enter your age : "))
if age<18:
    print("Not old enough to vote")
else:
    print("Old enough to vote")