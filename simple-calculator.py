print("== Simple Calculator ===")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+,-,*,/): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "invalid operator"

print("Result:", result)
