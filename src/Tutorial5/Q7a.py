# 7.a) Try the following nested for loop.
# 
#       for x in range(1,4): # print 3 rows
#           for y in range(1,4): # 3 asterisks in each row
#               print('*', end='')
#           print()
#
# The output is:
#   ***
#   ***
#   ***

for x in range(1, 4):
    for y in range(1, 4):
        print('*', end='')
    print()
