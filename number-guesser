import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get user input
            guess = int(input("Take a guess: "))
            attempts += 1
            
            # Check the guess against the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You found the number in {attempts} attempts!")
                break
                
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
