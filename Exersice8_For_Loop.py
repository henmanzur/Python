#############
# For Loops #
#############
'''
לולאות הן הדרך של כל שפת תוכנה לבצע פעולות חוזרות מספר פעמים.
דוגמה ללולאה מהעולם האמיתי היא שטיפת כלים, אנחנו לוקחים מס של כלים ומבצעים עליהם סדר פעולות דומה
שחוזר על עצמו בלולאה מספר פעמים.
יש שני סוגי לולאות :
לולאת for
ולולאת while

         לולאות for לדוגמא :
         ----------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

##########################################

for x in "banana":
    print(x)

##########################################

fruits = ["app", "ban", "chair"]
for x in fruits:
    print(x)
    if x == "ban":
    break

##########################################

for x in range(10):
    print(x)

##########################################

for x in range(5,10):
    print(x)

##########################################

fruits = ["apple", "banana"]
for x in fruits:
    if x == "banana":
    continue
    print(x)

##########################################

for x in range(2,30,3):
    print(x)

##########################################

'''
# תרגול :
# for x in range(1,11): # הלולאה תספור בטווח של 1 עד 11 לא כולל (1-10)
#     print(x)
#     print("wow\n")

# list_hen = ["banana", "apple", "mango"]
# for x in range(len(list_hen)):
#     print(list_hen[x])

# for x in range(2,30,3): # הלולאה תספור בטווח של 2 עד 30 לא כולל (2-29) בקפיצות של 3
#     print(x)
from time import sleep
print("\nNow we will get all the detailss about your class: \n--------------------------------------------------")
for i in range(4):
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))
    phone = input("Enter a phone: ")
    print("Printing student number " + str(i+1) + " Details...\n")
    sleep(3)
    print("Full Name: " + name + "\nAge: " + str(age) + "\nPhone: " + phone + "\n----------------------\n")

print("\nBye Bye..\n")