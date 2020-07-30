# Exercise 4
#   Rewrite exercise 3 so that it uses a Boolean variable (set to True or False) to control 
#   the loop. The user will still enter -9 to exit.

total = 0
count = 0
entered_num = 0
break_entered = False
while break_entered == False:
    entered_num = int(input("Please enter a number : "))
    if entered_num != -9:
        total = total + entered_num
        count = count + 1
    else:
        break_entered = True

if count != 0:
    average = total / count
    print(average)
else:
    print("No values were entered!")