import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

rows = 3
cols = 3

symbols_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 7
}

def get_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


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

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 and 3.")
        else:
            print("Invalid input. Please enter a numeric value.")
    
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a bet between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Invalid input. Please enter a numeric value.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(rows, cols, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = get_winnings(slots, lines, bet, symbols_count)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    
    # Calculate and store the new balance
    balance += winnings - total_bet
    print(f"Your balance is ${balance}")

    # Return the new balance so main() can use it
    return balance

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        play_again = input("Press enter to play (q to quit).")
        if play_again == "q":
            break
        balance = spin(balance)
    
    print(f"You left with ${balance}")
   
main()
