#   4. Type the following. Check the differences between the three print statements. 
#       the_text = input('Enter some text.\n') # get some text!

#           #print - version 1
#           print('This is what you entered: ')
#           print(the_text)

#           #print - version 2
#           print('This is what you entered:', the_text)

#           #print - version 3 - To supress printing of a new line, use end=' '
#           print('This is what you entered:', end=' ') print(the_text)

the_text = input('Enter some text. \n')
#print - version 1
print('This is what you entered: ')
print(the_text)
#print - version 2
print('This is what you entered: ', the_text)
#print - version 3
print('This is what you entered: ', end=' ')
print(the_text)