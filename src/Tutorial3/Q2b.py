#   b)	Test the solution you created in the lecture.
#       •	Write a program to display “FAIL” if the mark entered is less than 40%, 
#           otherwise it should display “PASS”.
#       •	Trace which lines would be printed for exam marks: 39, 40, 41

mark = int(input("Enter the mark : "))
if mark<40:
    print("FAIL")
else:
    print("PASS")