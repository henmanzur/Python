'''
####################
#### Exercise 2 ####
####################

2. Create a Lotto game:
 Puts in a list of 6 numbers, between 1-37, as in a real lottery.
 The numbers must not be repeated.
 Each game (row) in Lotto costs 3 ILS, Insert how much money do you have?
 Random 6 numbers – the winner's number.
 Then play few rounds (rows) as your budget can handle.
 On each round, random 6 numbers , between 1-37, and check if you won.
 In the end sum the entire prize from all rounds.

If you guess:
6 numbers = won 1M ILS
5 numbers = won 5000 ILS
4 numbers = won 100 ILS
3 numbers = won 10 ILS

'''
from random import randint
from time import sleep

lottoNumbers = []

for i in range (0,6):
    number = randint(1,37)
    while number in lottoNumbers:
        number = randint(1,37)

    lottoNumbers.append(number)

lottoNumbers.sort()

print("\n-------------------------------\n🎲 Welcome to my Lotto Game! 🎲\n    Each turn cost 3 ILS\n-------------------------------")
money = int(input("Enter How much money do you have: "))
turns = (money//3)
if(money >= 3):
    print("-------------------------------\nYou have: " + str(turns) + " turns\nYour change: " + str(money % 3) + " ILS\n")
    print("Lets Play!\n\n-------------------------------")
    sleep(2)
else:
    print("\n-------------------------------\nYou don't have enough money to play the lotto game.\n-------------------------------\nGood Bye!")
    exit()

userNumbers = []
for t in range(turns):
    userNumbers.clear()
    print("Round Number " + str(t + 1) + " :\n")
    for i in range (0,6):
        number = int(input("Please enter a number between 1-37: "))
        while (number in userNumbers or number < 1 or number > 37):
            print("Invalid number, The numbers must not be repeated.")
            number = int(input("Please enter a number between 1-37: "))
        userNumbers.append(number)

    print("-------------------------------\nToday's lottery numbers is: ")
    print(lottoNumbers)
    print("-------------------------------\nYour selection numbers:")
    print(userNumbers)

    counter = 0
    for number in userNumbers:
        if (number in lottoNumbers):
            counter += 1
    if (counter == 3):
        print("You won 10 ILS!!!\n")
    elif (counter == 4):
        print("You won 100 ILS!!!\n")
    elif (counter == 5):
        print("You won 5000 ILS!!!\n")
    elif (counter == 6):
        print("You won 1M ILS!!!\n")
    else:
        print("You LOSE!\n")
    print("you guessed " + str(counter) + " number/s correctly.\n-------------------------------\n")

'''
Github link -
https://github.com/henmanzur/Python/blob/master/Python%20Final%20Project/Exercise2.py
'''