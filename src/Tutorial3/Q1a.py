#   1.	Use if by itself to test a condition and do one set of actions if it is true 
#       otherwise do nothing.

#   a)	Type and run this example. Test with values: 99, 100, 101
#           n = int(input('Give me a number over 100: '))
#           if n <= 100:
#               print(n, 'is not over 100')

n = int(input("give me a number over 100 : "))
if n <= 100:
    print(n, 'is not over 100')