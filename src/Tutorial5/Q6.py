# 6.Nested for loops - A loop within a loop.
#   Try the following program and check you understand how the program runs the nested loop 
#   code.
#       for number in range(3) :
#           print("-------------------------------------------")
#           print("Outer loop iteration " + str(number))
#           # Inner loop
#           for another_number in range(4):
#               print("****************************")
#               print("In inner loop iteration " + str(another_number))

# Outer Loop
for number in range(3):
    print("--------------------------------")
    print("Outer loop iteration " + str(number))
    # Inner Loop
    for another_number in range(4):
        print("**********************")
        print("In inner loop iteration " + str(another_number))
