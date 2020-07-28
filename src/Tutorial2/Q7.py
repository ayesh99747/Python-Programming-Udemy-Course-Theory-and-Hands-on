#   7.	Temperature Program (part 1) – 
#   This program will be extended in a later tutorial.
#   Write a program that will convert a Centigrade temperature (c) entered as input into 
#   Fahrenheit (f) using the formula:  
#           f = (9/5)* c + 32

temp_c = input("Enter the temperature in celcius : ")
temp_f = (9/5) * int(temp_c) +32
print("Temperature in farenheit is", temp_f)