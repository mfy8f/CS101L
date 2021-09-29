num_3 = 0
num_5 = 0
num_7 = 0
play = True
print('Welcome to the Flarsheim Guesser!')
print('Please think of a number between and including 1 and 100.')
while play == True:
    num_3 = 0
    num_5 = 0
    num_7 = 0
    while play == True:
        num_3 = int(input('What is the remainder when your number is divided by 3 ?'))
        if num_3 < 0:
            print('The value entered must be 0 or greater')
        elif num_3 > 3:
            print('The value entered must be less than 3')
        else:
            break
    while play == True:
        num_5 = int(input('What is the remainder when your number is divided by 5 ?'))
        if num_5 < 0:
            print('The value entered must be 0 or greater')
            continue
        elif num_5 > 4:
            print('The value entered must be less than 4')
            continue
        else:
            break
    while play == True:
        num_7 = int(input('What is the remainder when your number is divided by 7 ?'))
        if num_7 < 0:
            print('The value entered must be 0 or greater')
            continue
        elif num_7 > 6:
            print('The value entered must be less than 6')
            continue
        else :
            break
    for cnt in range(1, 101):
        if cnt % 3 == num_3 and cnt % 5 == num_5 and cnt % 7 == num_7:
            print("Your number was ", cnt)
            print("How amazing is that?")
            print()
            break
    while True:
        response = input("Do you want to play again? Y to continue, N to quit  ==> ")
        if response.upper() == "Y":
            break
        if response.upper() == "N":
            play = False
            break
