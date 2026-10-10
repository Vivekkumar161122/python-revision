# User se 3 number lekar averge 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

avg = (num1 + num2 + num3) / 3
print(f"Average: {avg}")

# T5 subjects ke marks input lekar total aur percentage
m1 = float(input("Enter Subject 1 marks: "))
m2 = float(input("Enter Subject 2 marks: "))
m3 = float(input("Enter Subject 3 marks: "))
m4 = float(input("Enter Subject 4 marks: "))
m5 = float(input("Enter Subject 5 marks: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

print(f"Total Marks: {total}/500")
print(f"Percentage: {percentage}%")

# TSalary aur bonus input lekar total salary calculate karo
salary = float(input("Enter base salary: "))
bonus = float(input("Enter bonus: "))

total_salary = salary + bonus
print(f"Total Salary: {total_salary}")

# Number input lekar uska square aur cube print karo.
num = float(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print(f"Square: {square}")
print(f"Cube: {cube}")

# Minutes ko hours + remaining minutes mein convert
total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{hours} Hours and {minutes} Minutes")

# Seconds ko hours, minutes aur seconds mein convert 
total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
remaining_sec = total_seconds % 3600
minutes = remaining_sec // 60
seconds = remaining_sec % 60

print(f"{hours} Hours, {minutes} Minutes, {seconds} Seconds")
