'''
לבנות 4 פונקציות
פונקציה 1 ל MENU
פונקציה 2 כשלוחצים על 1
פונקציה 3 כשלוחצים על 2
ופונקציה 4 כשלוחצים על 3
להכין תפריט שבתפריט שיראה כך :
Menu:
1.Dogs Details
2.Friends list
3.N Azzeret (Factorial)

בתוך קטגוריית dog details יהיו פרטים וגיל של הכלבים וכשנבחר באחד הכלבים הגיל יוכפל ב7 כדי שנראה בן כמה הוא בגיל של בני אדם

בתוך קטגוריית Friend list יוצר רשימה של 5 חברים שאני קולט אותם כל פעם בלולאה ואחר כך אני קולט עוד חבר אם החבר שאני קולט נמצא בתוך הרשימה
תירשם הודעה שהוא נמצא ואם לא אז שירשם שהוא לא נמצא

נקלוט מספר ונכפיל אותו מ1 עד המספר עצמו ונרשום תוצאה
לדוגמה :
קלטתי מספר 7
אז נכפיל 7*1, 7*2 7*3 7*4 7*5 7*6 7*7 ונרשום תוצאה
'''
def Menu():

    while (True):
        choose = input("\nMenu: \n1.Dogs Details\n2.Friends List\n3.N Azzeret\n\nEnter a number: ")

        if(choose == "1"):
            DogDetails()
        elif(choose == "2"):
            FriendsList()
        elif(choose == "3"):
            N_Azzeret()
        else:
            print("\nchoose 1-3 only!!")
            continue
        BackMenu = input("Do you want get back to menu? yes/no\n")
        if (BackMenu == "yes" or BackMenu == "y"):
            print("\nWelcome Back!")
            continue
        else:
            print("\nGood Bye.")
            break

def DogDetails():
    while (True):
        dog1 = "Rex"
        dog1_age = 3
        dog2 = "Nike"
        dog2_age = 4
        dog3 = "Bobby"
        dog3_age = 5
        choose = input("\nDogs Details:\n------------\n1.Name: " + dog1 + " | Age: " + str(dog1_age) + "\n\n2.Name: " + dog2 + " | Age: "\
                       + str(dog2_age) + "\n\n3.Name: " + dog3 + " | Age: " + str(dog3_age) + "\n------------\nEnter a number: \n")

        if (choose == "1"):
            print("\n" + dog1 + " is " + str(dog1_age) +" years old and at the age of humans he is: " + str(dog1_age * 7) + " years old!")
        elif (choose == "2"):
            print("\n" + dog2 + " is " + str(dog2_age) +" years old and at the age of humans he is: " + str(dog2_age * 7) + " years old!")
        elif (choose == "3"):
            print("\n" + dog3 + " is " + str(dog3_age) +" years old and at the age of humans he is: " + str(dog3_age * 7) + " years old!")
        else:
            print("\nchoose 1-3 only!!")
            continue
        exit = input("\nDo you want to exit? yes/no\n")
        if (exit == "yes" or exit == "y"):
            break

def FriendsList():
    friend_list = []
    print("\nIn this category you can add friends to your friends list\n----------------------------------------------")
    while(True):
        for i in range(5):
            friend_list.append(input("Enter a friend's name: "))
        name = input("\nEnter a new name of friend: ")
        if (name in friend_list):
            print("\n" + name + " is already in your Friend list.")
            print("This is your Friend list: " + str(friend_list))
        else:
            friend_list.append(name)
            print("\n" + name + " added to your friend list!")
            print("This is your new Friend list: " + str(friend_list))

        exit = input("\nDo you want to exit? yes/no\n")
        if (exit == "yes" or exit == "y"):
            break
        else:
            continue

def N_Azzeret():
    while(True):
        num = int(input("Enter a number to calculate his Azzeret: "))
        sum = 1
        for i in range(1, num + 1):
            sum = sum * i

        print(str(num) + " Azzeret is: " + str(sum) + "\n")

        exit = input("\nDo you want to exit? yes/no\n")
        if (exit == "yes" or exit == "y"):
            break
        else:
            continue

##############################################-----MAIN-----##############################################

Menu()
