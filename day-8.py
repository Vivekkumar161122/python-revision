# Strings are generally sequences, Strings are immutable.
''' Immutable means id once we have assign a character value to a particular index
then we cannot change it'''
''' p is 0, y is 1, t is 2, h is 3, o is 4 and n is 5 '''
word = "python"
print(word[2])

# Printing each character value
word = "Python"
for ch in word:
    print(ch)

# Slicing a string
''' if we need a particular part of a string that process is called slicing '''
word = "Python"
print(word[2:4])
