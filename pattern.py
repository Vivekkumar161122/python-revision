# Write a python program to print the following pattern:
'''
1
22
333
4444
55555
'''
for i in range(1,6):
  for j in range(i):
    print(i, end = " ")
  print()

print()

# New Approach
for i in range(1,6):
  # for j in range(i):
  #   print(i, end = " ")
  print(str(i)*i)

print()
print(str(1)*4)
