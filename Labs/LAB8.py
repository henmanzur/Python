###############
## Fibonacci ##
###############
'''
ניצור רשימה (list) בשם fibo וברשימה נרשום מספרים אך שאחרי כל 2 תאים המספר בתא ה3 יהיה שווה ל2 לפניו
לדוגמא :
fibo = [1,2,3,5,8,13,21]
fibo2 = [2,9,11,20,31,51]
c=a+b
כל ספרה שווה ל2 שלפנייה

התרגיל מעבדה:
1.
תוכנה שתבדוק אם הlist הוא Fibonucci
2.
ליצור Menu
1.printing 100 numbers
2.check fibo
3.randint numbers until we get 12 or we count 10 times
'''
# 1.
# fibo = [1,2,3,5,8,13,21]
#
# boolean = "True" # משתנה שבדרך כלל הוא True או False
# for i in range(2,len(fibo)):
#     print(fibo[i]) # בודק את המספר ה3
#     print(fibo[i-1]) # מה שלפניו
#     print(fibo[i-2]) # מה שלפניו
#     print("\n")
#     if (fibo[i] != (fibo[i-1]+fibo[i-2])):
#         boolean = "False"
#         break
#
# if (boolean == "True"):
#     print("It is fibo series")
# else:
#     print("it isn't fibo series")

from random import randint
from time import sleep

choise = input("Menu: \n1.printing 100 numbers\n2.check fibo\n3.randint numbers until we get 12 or we count 10 times\nChoose 1-3 from the menu: \n")

if (choise == "1"):
    print("Printing 1-100...")
    sleep(3)
    for i in range(1,101):
        sleep(0.5)
        print(i)
elif (choise == "2"):
    fibo = [1,2,3,5,8,13,21]
    print("\n" + str(fibo))
    print("Checking if this list is Fibonacci...")
    sleep(3)
    boolean = "True" # משתנה שבדרך כלל הוא True או False
    for i in range(2,len(fibo)):
        print(fibo[i]) # בודק את המספר ה3
        print(fibo[i-1]) # מה שלפניו
        print(fibo[i-2]) # מה שלפניו
        print("\n\n")
        if (fibo[i] != (fibo[i-1]+fibo[i-2])):
            boolean = "False"
            break

    if (boolean == "True"):
        print("It is Fibonacci series")
    else:
        print("it isn't Fibonacci series")
elif (choise == "3"):
    print("\n------------------------\nYou have 10 chances to get the number 12 on random numbers...\n------------------------\n")
    sleep(3)
    counter = 10
    for i in range(counter):
        print("Round Number: " + str(i+1) + "\n")
        sleep(3)
        random_num = randint(1, 12)
        print("The random number you got is : " + str(random_num))
        if (random_num == 12):
            print("You are so lucky! you got number 12 !\n------------------------")
            break
        else:
            print("You are so unlucky you didn't got number 12 !\n------------------------")
else:
    print("Choose 1-3 Only!!")