from random import randint # ספריית הגרלת מספרים רנדומלים
from time import sleep # משיכת פונקציה ליצירת sleep
print("\nGetting random numbers...")
num1 = randint(1,37) # מגריל מספר מ1 עד 37
num2 = randint(1,37)
sleep(3)
print("1st Number: " + str(num1) + "\n2nd Number: " + str(num2))

if num1 == num2:
    print("You Won 100$!!\n")
else:
    print("You lose!!\n")

print("Bye Bye.\n")