# Evaluate and print the results of the expression: X = 10 + 3 * 2 * * 2. Based on what you learnt in the lecture, explain why the output is what it is.
x = 10 + 3 * 2 ** 2
print(x)

# Ask the user for a temperature in celcius and convert it to float. Convert it to float, then calculate and print the temperature in fahrenheit.
celcius_str = input("Enter temperature in Celcius: ")
celcius_temp = float(celcius_str)
fahrenheit_temp = (celcius_temp * 9/5) + 32
print(f"the temperature in fahrenheit is: {fahrenheit_temp}")

# Write a program to swap values of two numbers entered by the user.
''' In python swapping variables is incredibly clean because you can tuples assignment tp swap them in a single line without needing a temporary third varable. ''' 
''' Taking two numbers as input from the user ''' 
num1 = input("Enter the first number(num1): ")
num2 = input("Enter the second number(num2): ")
print(f"/nBefore swapping:: {num1} and {num2}")
''' The pythonic way to swap values ''' 
num1, num2 = num2, num1
print(f"After swapping: num1 = {num1}, num2 = {num2}")

# Ask the user to enter two integer and on float. Convert them al to float and print their average.
''' Taking input from the user ''' 
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = float(input("Enter a float number: "))
''' Converting all inputs to floats '''
val1 = float(num1)
val2 = float(num2)
val3 = float(num3)
''' Calculating the average '''
average = (val1 + val2 + val3) / 3
''' Printing the result ''' 
print(f"The average of the three numbers is: {average}")

# Explaination 
'''input(): Python always reads user input as a string. data type.'''
'''float(): since you cannot perform mathematical equation directly on text strings, we explicitly convert it into a floating-point decimal number.''' 
'''Calculation: python executes the operations insidde the parameters first (9/5), multiplies it by your celcius value and finallyy adds 32.'''
