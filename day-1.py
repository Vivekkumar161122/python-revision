# Create a string variable and print it's length
text = " Hello Python"
print(len(text))

# Take a name as input and print it in uppercase
name = input(" Enter name: ")
print(name.upper())

# Take a name as input and print it in lowercase
name = input("Enter name: ")
print(name.lower())

# Take a sentence and count the letter 'a'
sentence = "Data Structure and Alogorithms"
print(sentence.lower().count('a'))

# Count vowels in a sentence
sentence = "Python Programming"
vowels = "aeiouAEIOU"
count = sum(1 for char in sentence if char in vowels)
print("Vowel count:", count)

# Reverse a string without using reverse()
text = "python"
reversed_text = text[::-1]
print(reversed_text)

# Check whether a string is a palindrome
word = "radar"
is_palindrome = word.lower() == word.lower()[::-1]
print("Is palindrome:", is_palindrome)

# Count words in a sentence
sentence = "Learn Python for Machine Learning"
word_count = len(sentence.split())
print("Word count:", len(words))
