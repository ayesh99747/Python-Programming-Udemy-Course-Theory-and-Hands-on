#   Question 4. 
#   Write the Python program using the pseudocode shown.
#       INPUT cost_of_item
#       INPUT cash_paid (e.g., 10 for £10)
#       CALCULATE change

cost_of_item = input("Enter the cost of the item : ")
cash_paid = input("Enter the cash paid : ")
change = int(cash_paid) - int(cost_of_item)
print("The change is :", change)