def number_guesser():
    print("Think of a number between 1 to 100 in your mind!")
    input("Press Enter when you are ready...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) //2
        attempts += 1
        print(f"\nIs your number {guess}?")
        feedback = (
            input("Enter 'h' (too high), 'l' (too low) or 'c' (correct):")
            .strip()
            .lower()
        )

        if feedback == "c":
            print(f"\nAI found your number in {attempts} attempts!")
            break
        elif feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1
        else:
            print("Invalid input. Please enter 'h', 'l' or 'c'.")

number_guesser()
