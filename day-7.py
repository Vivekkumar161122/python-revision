# Principal, rate aur time input lekar simple interest calculate 
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (in years): "))

si = (p * r * t) / 100
print(f"Simple Interest: {si}")

# Distance aur time input lekar speed calculate 
distance = float(input("Enter distance (in km): "))
time = float(input("Enter time (in hours): "))

speed = distance / time
print(f"Speed: {speed} km/h")

# Number positive, negative ya zero check 
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Number even ya odd check 
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Age input lekar check karo ki person vote kar sakta hai ya nahi.
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Number check karo ki 5 se divisible hai ya nahi.
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# Do numbers mein bada number find 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is larger")
elif num2 > num1:
    print(f"{num2} is larger")
else:
    print("Both numbers are equal")
