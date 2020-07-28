#   c)	Tip Calculator – A restaurant wants to suggest a tip according to the service 
#       diners receive. Write a program that calculates a tip according to the 
#       diner’s satisfaction.

#       •   Ask the diner to enter the cost of the meal.
#       •	Ask the diners’ satisfaction level using ratings: 1 = Totally satisfied, 
#           2 = Satisfied, 3 = Dissatisfied.
#       •	If the diner is totally satisfied (1), calculate a 20 percent tip.
#       •	If the diner is satisfied (2), calculate a 15 percent tip.
#       •	If the diner is dissatisfied (3), calculate a 10 percent tip.
#       •	Report the satisfaction level and tip. Your solution should use an 
#           if, elif, else.

cost_of_the_meal = int(input("Enter the cost of the meal : "))
satisfaction_level = input("Enter the satisfaction level : ")
if satisfaction_level == '1':
    tip = cost_of_the_meal * (20/100)
    print("The customer is totally satisfied.")
    print("The tip is : ", tip)
elif satisfaction_level == '2':
    tip = cost_of_the_meal * (15/100)
    print("The customer is satisfied.")
    print("The tip is : ", tip)
elif satisfaction_level == '3':
    tip = cost_of_the_meal * (10/100)
    print("The customer is dissatisfied.")
    print("The tip is : ", tip)
else:
    print("Invalid satisfaction level")