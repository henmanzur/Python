# Function of lottery numbers generator machine(auto lottery ticket)

from random import randint
#############Lines###############
Line1 = []
Strong1 = []
Line2 = []
Strong2 = []
Line3 = []
Strong3 = []
Line4 = []
Strong4 = []
Line5 = []
Strong5 = []
Line6 = []
Strong6 = []
#################################

def LotteryGenerate():

    for line in range (0,6):
        number = randint(1,37)
        while number in Line1:
            number = randint(1,37)
        Line1.append(number)

        number2 = randint(1, 37)
        while number2 in Line2:
            number2 = randint(1, 37)
        Line2.append(number2)

        number3 = randint(1, 37)
        while number3 in Line3:
            number3 = randint(1, 37)
        Line3.append(number3)

        number4 = randint(1, 37)
        while number4 in Line4:
            number4 = randint(1, 37)
        Line4.append(number2)

        number5 = randint(1, 37)
        while number5 in Line5:
            number5 = randint(1, 37)
        Line5.append(number5)

        number6 = randint(1, 37)
        while number6 in Line6:
            number6 = randint(1, 37)
        Line6.append(number6)

    for strong in range (1):

        number1 = randint(1,7)
        while number1 in Strong1:
            number1 = randint(1,7)
        Strong1.append(number1)

        number2 = randint(1, 7)
        while number2 in Strong2:
            number2 = randint(1,7)
        Strong2.append(number2)

        number3 = randint(1, 7)
        while number3 in Strong3:
            number3 = randint(1,7)
        Strong3.append(number3)

        number4 = randint(1, 7)
        while number4 in Strong4:
            number4 = randint(1,7)
        Strong4.append(number4)

        number5 = randint(1, 7)
        while number5 in Strong5:
            number5 = randint(1,7)
        Strong5.append(number5)

        number6 = randint(1, 7)
        while number6 in Strong6:
            number6 = randint(1,7)
        Strong6.append(number6)


    print(" \n--- Lottery Generator ---\n---------------------------\n" + "Line 1 : " + str(Line1) + " " + str(Strong1)
          + "\n---------------------------\n" + "Line 2 : " + str(Line2) + " " + str(Strong2)
          + "\n---------------------------\n" + "Line 3 : " + str(Line3) + " " + str(Strong3)
          + "\n---------------------------\n" + "Line 4 : " + str(Line4) + " " + str(Strong4)
          + "\n---------------------------\n" + "Line 5 : " + str(Line5) + " " + str(Strong5)
          + "\n---------------------------\n" + "Line 6 : " + str(Line6) + " " + str(Strong6)
          + "\n---------------------------\n" +" --- Good Luck ! ---")

