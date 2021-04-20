'''
LAB 7 - Cube Project
נקבל כקלט כמה כסף יש לנו לשחק
עלות משחק 3 ש"ח
אם יש עודף נחזיר אותו ללקוח
בכל תור נגריל 2 קוביות, אם הן זהות זכינו ב100 ש"ח, אם הן זהות אבל שוות גם ל6 זכינו ב1000 ש"ח
אם הן לא זהות, אבל קוביה 2 שווה ל-2 זכינו ב40 ש"ח
אם הן לא זהות, אבל קוביה 1 שווה ל-1 זכינו ב20 ש"ח
לבסוף נדפיס למסך בכמה כסף זכינו
'''
from random import randint
from time import sleep

print("\n-------------------------------\n🎲 Welcome to my Cube game! 🎲\n    Each turn cost 3 ILS\n-------------------------------")
money = int(input("Enter How much money do you have: "))
turns =(money//3)

sleep(2)
if(money >= 3):
    print("-------------------------------\nYou have: " + str(turns) + " turns\nYour change: " + str(money % 3) + " ILS\n")
    print("Lets Play!\n\n-------------------------------")
    sleep(3)
else:
    print("\n-------------------------------\nYou don't have enough money to play the cubes game.\n-------------------------------")

price = 0
for i in range(turns):
    print("Round Number " + str(i+1) + " :")
    print("The Dealer Rolling the Cubes...\n")
    sleep(3)
    cube1 = randint(1, 6)
    cube2 = randint(1, 6)
    print("Cube 1: " + str(cube1) + " \nCube 2: " + str(cube2))
    if (cube1 == cube2):
        if (cube1 == 6 and cube2 == 6):
            price = price + 1000
            print("\nYou got a double six !! You won 1000 ILS\n")
            print("You have now: " + str(money % 3 + int(price)) + " ILS, includes your change.\n-------------------------------")
        else:
            price = price + 100
            print("\nYou got a double !! You won 100 ILS\n")
            print("You have now: " + str(money % 3 + int(price)) + " ILS, includes your change.\n-------------------------------")
    elif (cube1 == 1 and cube2 == 2):
        price = price + 60
        print("\nYou got a 1 on Cube 1 and 2 on Cube 2!! You won 60 ILS\n")
        print("You have now: " + str(money % 3 + int(price)) + " ILS, includes your change.\n-------------------------------")
    elif (cube1 == 1):
        price = price + 20
        print("\nYou got a 1 on Cube 1 !! You won 20 ILS\n")
        print("You have now: " + str(money % 3 + int(price)) + " ILS, includes your change.\n-------------------------------")
    elif (cube2 == 2):
        price = price + 40
        print("\nYou got a 2 on Cube 2 !! You won 40 ILS\n")
        print("You have now: " + str(money % 3 + int(price)) + " ILS, includes your change.\n-------------------------------")
    else:
        print("\nYou LOSE !\n-------------------------------")

print("You won this game for: " + str(price) + " ILS\n")
print("Good Bye!\n\n")