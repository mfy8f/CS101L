import random
def play_again() -> bool:
    while True:
        a = input('Do you want to play again? Y/Yes or N/No')
        if a.upper() == 'Y' or 'YES':
            return True
        if a.upper() == 'N' or 'NO':
            return False
        else:
            print('You must enter Y/Yes or N/No')
     
def get_wager(bank : int) -> int:
    while True:
        wager_amount = int(input('amount of chips for wager?'))
        if wager_amount <= 0:
            print('Input an amount more than 0')
            continue
        if wager_amount > bank:
            print('The entered amount is greater than the amount you have')
            continue
        else: 
            return wager_amount
        ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''           

def get_slot_results() -> tuple:
    reel1 = random.randint(0,11)
    reel2 = random.randint(0,11)
    reel3 = random.randint(0,11)
    ''' Returns the result of the slot pull '''
    return reel1, reel2, reel3

def get_matches(reel1, reel2, reel3) -> int:
    if reel1 == reel2 and reel1 == reel3 and reel2 == reel3: 
        return 3
    if reel1 != reel2 and reel1 != reel3 and reel2 != reel3:
        return 0 
    else:
        return 2
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''

def get_bank() -> int:
    bank = 100
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    return bank

def get_payout(wager, matches):
    if matches == 3:
        return wager * 10
    if matches == 2:
        return wager * 3 
    else:
        return wager * -1
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''


if __name__ == "__main__":
    total_value = 0
    total_value = total_value + 100
    playing = True
    while playing == True:

        bank = get_bank()
        count = 0 #Added a count for playing
        list_bank = []
        total_value = total_value

        while bank >0:  # Replace with condition for if they still have money.        
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            count +=1
            list_bank.append(bank)
            if total_value <0:
                continue
            total_value = total_value + payout
        max_value = max(list_bank)
        total_value = total_value
           
        print(f"You lost all", total_value, "in", count, "spins")
        print(f"The most chips you had was", max_value)
        playing = play_again()