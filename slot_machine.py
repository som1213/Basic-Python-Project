import random
def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']

    result = [] 
    for symbol in range (3) :
        result.append(random.choice(symbols))
    return result
    # return[random.choice(symbols) for _ in range(3)]
    
def print_row(row):
    print("*************************")
    print(" | ".join(row))
    print("*************************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2] :
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100
    print("********************************")
    print(" This is a slot machine program ")
    print(" Symbals   🍉  🍋  🔔  ⭐  🍒 ")
    print("********************************")

    while balance > 0:
        print(f"Current balance is {balance}")

        bet = input("place your bet amount :")
        if not bet.isdigit():
            print("Please Enter a valid number")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient Amount !")
            continue
        if bet <= 0:
            print("bet must be gareter then 0 ")
            continue
        balance -= bet
# part 01 completed
        row = spin_row()   
        print("Spinning.....\n")
        print_row(row)
        payout = get_payout(row,bet)
        if payout > 0 :
            print(f"You Won ${payout} !")
        else:
            print("Sorry You lost this round ")
        balance += payout

        play_again = input("Do you want to spin again ?(Y/N) :").upper()
        if play_again != "Y":
            break

    print (f"Game over ! Your final balamce is ${balance}") 

if __name__=='__main__':
    main()