# Take a radius (r) as user input and print the area. 
''' Take the radius (r) as user input and convert it to a float '''
radius_str = input("Enter the radius of the circle: ")
r = float(radius_str)
''' Define the value of Pi '''
pi = 3.14
''' Calculate the area using the formula: Area = pi * (rsquared)'''
area = pi * (r ** 2)
''' Print the calculated area'''
print(f"The area of the circle with the radius {r}is: {area}")

# Key concept
''' float(radius_str): We convert the input into a float so the program can handle radius values with decimals (like 5.5) '''
   
# Ask the user for: Principal (P), Rate (R), Time(T). Convert all to float and compute simple interest: SI = (P*R*T)/100
''' Taking input from the user '''
P = float(input("Enter the Principal amount (P): "))
R = float(input("Enter the rate of interest (R): "))
T = float(input("Enter the time period in years(T): "))
''' Calculate Simple Interest '''
SI = (P * R * T) / 100
''' Printing the result '''
print(f" The Simple Interest (SI) is: {SI}")
