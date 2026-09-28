balance = 10000.0
correct_pin = "1234"

pin = input("Enter your 4-digit PIN: ")

if pin != correct_pin:
    print("Incorrect PIN. Access Denied!")
else:
    while True:
        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == "1":
            print(f"Current Balance: ₹{balance:.2f}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount:.2f} deposited successfully. New Balance: ₹{balance:.2f}")
            else:
                print("Invalid amount!")
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Invalid amount!")
            elif amount > balance:
                print("Transaction Failed: Insufficient Balance!")
            else:
                balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully. Remaining Balance: ₹{balance:.2f}")
        elif choice == "4":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")
