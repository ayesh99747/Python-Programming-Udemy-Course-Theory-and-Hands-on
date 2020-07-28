#   4.	
#   Note :  elif (chained conditional) allows you to give the program additional conditions. 
#           Only the first true branch runs. If none of the conditions match then run the 
#           else-block (optional).

#   a)	Temperature Program (part 2) Extend the program created for tutorial 2. The program 
#       should do the following.
#       •	Ask the user to enter ‘1’ if they want to convert from Celsius to Fahrenheit 
#           or enter ‘2’ if they want to convert from Fahrenheit to Celsius.
#       •	Ask the user to enter a temperature in the correct unit.
#       •	Formulas:
#               f = (9/5) * c + 32
#               c = (f-32) * 5 / 9
#       •	Apply the conversion formula and display the temperature in the new unit.
#       •	Use an if to check if the user has entered ‘1’ , an elif to check if the 
#           user has entered ‘2’ and an else to display ‘invalid option entered’.

temperature_unit = int(input("Enter '1' to calculate from celcius to farenheit or enter '2' to calculate farenheit to celcius: "))
if temperature_unit == 1:
    temperature_c = int(input("Enter the temperature in celcius : "))
    temperature_f = (9/5) * temperature_c + 32
    print(temperature_f)
elif temperature_unit == 2:
    temperature_f = int(input("Enter the temperature in farenheit : "))
    temperature_c = (temperature_f-32) * 5 / 9
    print(temperature_c)
else:
    print('Invalid Option entered!')