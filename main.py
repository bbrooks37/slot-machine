def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive amount greater thn 0.")
        else:
            print("Invalid input. Please enter a numeric value.")
    
    return amount

deposit()
