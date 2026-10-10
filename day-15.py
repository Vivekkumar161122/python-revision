'''Find all duplicates elements in a list alongwith their frequencies. '''
lst = [1, 2, 3, 2, 4, 5, 3, 2, 6, 5]
feq = {}

for i in lst:
    if i in feq:
        feq[i] += 1  # Fixed: needs reassignment
    else:
        feq[i] = 1

for key in feq:
    if feq[key] > 1:
        print(key, ";", feq[key])

'''Write a program to print a pattern.'''
for i in range(1,4):
    print("*" * i)

for i in range(2,0, -1):
    print("*" * i)

# Write a Python program to print a heart shape pattern using (*).
for i in range(6):
    for j in range(7):
        if (i == 0 and j % 3 != 0) or \
            (i == 1 and j % 3 == 0) or \
            (i - j == 2) or \
            (i + j == 8):
             print("*", end=" ")
        else:
             print(" ", end=" ")
    print() 
