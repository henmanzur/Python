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
    print("The dealer threw the cubes...\n")
    sleep(3)
    cube1 = randint(1, 6)
    cube2 = randint(1, 6)
    print("Cube 1: " + str(cube1) + " \nCube 2: " + str(cube2))
    a1000 = 1000
    a100 = 100
    a60 = 60
    a40 = 40
    a20 = 20
    if (cube1 == 6 and cube2 == 6):
        print("\nYou won " + str(a1000) + " ILS !")
        print("You have now: " + str(money % 3 + int(a1000)) + " ILS, includes your change.\n-------------------------------")
    elif (cube1 == cube2):
        print("\nYou won " + str(a100) + " ILS !")
        print("You have now: " + str(money % 3 + int(a100)) + " ILS, includes your change.\n-------------------------------")
    elif (cube1 == 1 and cube2 == 2):
        print("\nYou won " + str(a60) + " ILS !")
        print("You have now: " + str(money % 3 + int(a60)) + " ILS, includes your change.\n-------------------------------")
    elif (cube1 != cube2 and cube1 == 1):
        print("\nYou won " + str(a20) + " ILS !")
        print("You have now: " + str(money % 3 + int(a20)) + " ILS, includes your change.\n-------------------------------")
    elif (cube2 != cube1 and cube2 == 2):
        print("\nYou won " + str(a40) + " ILS !")
        print("You have now: " + str(money % 3 + int(a40)) + " ILS, includes your change.\n-------------------------------")
    else:
        print("\nYou lose !\n-------------------------------")

print("\nGood Bye!\n")