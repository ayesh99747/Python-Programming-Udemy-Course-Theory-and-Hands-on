#   b)	Create a simple calculator program in Python. 
#       The calculator should resolve simple arithmetic expressions by the user entering:
#       •	An integer (e.g., 6)
#       •	One of the operators `+', `-', `*' or `/' (e.g., *)
#       •	Another integer (e.g., 4)
#               o	E.g., to give the expression 6*4
#       •	The program should calculate the value of the expression entered and display 
#           the result.
#       •	Add a test to ensure you do not divide by zero where appropriate. Hint: use 
#           a nested if else.
#       •	Use the following data to test your program

#      ______________________________________________________
#      | Integer 1	| Operator | Integer 2 | Expected Result |
#      ______________________________________________________
#      |     3	    |     +    |      2    |	   5         |
#      |     3	    |     -    |      2    |	   1         |
#      |     3	    |     *    |      2    |	   6         |
#      |     3	    |     /    |      0    |	 Error       |
#      |     3	    |     /    |      2    |	  1.5        |
#      ______________________________________________________

num1 = int(input("Enter the 1st integer : "))
operator = input("Enter the operator : ")
num2 = int(input("Enter the 2nd integer : "))
if operator=='+':
    result = num1 + num2
    print('The answer is : ', result)
elif operator=='-':
    result = num1 - num2
    print('The answer is : ', result)
elif operator=='*':
    result = num1 * num2
    print('The answer is : ', result)
elif operator=='/':
    if num2 == 0:
        print("Zero Division Error!")
    else:
        result = num1 / num2
        print('The answer is : ', result)