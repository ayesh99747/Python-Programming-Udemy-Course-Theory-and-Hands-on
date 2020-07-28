#   6.	Challenge Question - Create a program using an if, elif, else

#       •	Ask the user ‘Do you like Python? (yes/no): ’
#       •	If the user responds with ‘yes’ give an appropriate message (e.g. you are 
#           on the right course)
#       •	If the user responds with ‘no’ give an appropriate message (e.g., you might 
#           change your mind)
#       •	If the user gives a different response give an appropriate message (e.g., I 
#           did not understand).
#       •	Run and test your program. Then amend the program to accept additional ways 
#           of saying yes and no, e.g. Yes/No, y/n, etc
#       •	Experiment with the Python string methods upper() and lower() and check how 
#           they can improve your solution. Hint: if the users response is stored in 
#           a variable called response use: response = response.lower()

response = input("Do you like Python? (yes/no) : ")
response = response.lower()
if response == 'yes' or response == 'y':
    print("You are on the right course!")
elif response == 'no' or response == 'n':
    print("You might change your mind!")
else:
    print("I did not understand you.")