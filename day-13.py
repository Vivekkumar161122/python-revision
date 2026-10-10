# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# looping through a string
for x in "banana":
    print(x)

# Break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Don't print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range function
for x in range(6):
    print(x)
