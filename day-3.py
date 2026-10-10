# Multiple of 5
n = int(input(" enter num: "))
if (n % 5 == 0):
    print("multiple of 5")
else:
    print("not multiple of 5")

# Nesting
username = input("enter username: ")
password = input("enter password: ")

if (username == "vivek" and password == "1111"):
    print(" Success")
else:
    if(username != "admin"):
        print("wrong username")
    else:
            print("wrong password")

# Print reverse counting
''' reverse counting'''
i = 5
while (i >= 1):
    print(i)  

# print number 1 to 5
''' finite loop => 5x '''
i = 1 
while (i <= 5):
    print(i)
    i += 1

# Conditional statement
color = (input("Enter your color: "))
if color == "Green":
    print("GO")
elif color == "Yellow":
    print("SLOW DOWN")
elif color == "Red":
    print("STOP")
else:
    print("WRONG COLOR")
