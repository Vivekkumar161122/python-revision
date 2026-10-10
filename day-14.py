'''
Write a Python program that uses a for loop to iterate through numbers from 1 to 100,
and uses an if-else condition to display whether each number is even or odd.
'''
for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")

# simple
x = [1, 2, 3]
y = x
y.append(4)
print(x)
