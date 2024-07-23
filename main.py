import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET=1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":5,
    "C":5,
    "D":5
}

def check_winnings(columns,lines,bets,value):  
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column  in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol] * bets
            winning_lines.append(line + 1)
    
    return winnings,winning_lines



def get_slotmachine_spin(rows,cols,symbols):
    all_symbols =[]

    for symbol,symbol_count in symbols.items():
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


def print_slotmachine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        
        print()
def deposit():

    while True:
        amount = input("Please Enter the Amount :")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be Greater than Zero")
        else:
            print("Please Enter Valid Input")
        
    return amount

def get_number_of_lines():
    while True:
        lines = input("Please Enter Number of Lines to bet on:")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter Valid No of Lines")
        else:
            print("Please Enter Valid Input")
        
    return lines

def get_bet():
    while True:
        bet = input("How much you would like to bet on each line :")

        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter bet Between {MIN_BET} to {MAX_BET}")
        else:
            print("Please Enter Valid Input")
        
    return bet


def spin(balance):

    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_amount = lines * bet

        if total_amount > balance:
            print(f"You do not have enough money to bet.Your Current Balance is {balance}")
        else:
            break

    print(f"You have bet {bet} on {lines} lines.Total Bet is {total_amount}")

    slots = get_slotmachine_spin(ROWS,COLS,symbol_count)
    print_slotmachine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You Won {winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_amount



def main():
    balance = deposit()
    while True:
        print(f"Current Balance is {balance}")
        answer = input("Press Enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with {balance}")
        
    

main()
