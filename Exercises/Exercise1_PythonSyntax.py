                                    #Python Syntax
                                    ## סוגי משתנים

a=12
b=11.56
c="hen manzur"
#This is Integer(int) - משתנה מספר שלם
print(a)
print(type(a)) #type = לבדיקת סוג המשתנה
print("\n")
#This is Float - משתנה מספר לא שלם
print(b)
print(type(b)) #type = לבדיקת סוג המשתנה
print("\n")
#This is String(str) - משתנה מחרוזת
print(c)
print(type(c)) #type = לבדיקת סוג המשתנה
print("\n")

                                   # הדפסות
# לא ניתן להדפיס מחרוזת + מספר אלא רק מחרוזת + מחרוזת
name="Hen"
age="27"
intage=27
print("Hello " + name + "\nHow are you?\nYour age is: " + str(intage)) #str(int) על מנת להדפיס משתנה מחרוזת + משתנה מספר נשתמש בהמרה
print("\n")
print("Hello " + name + "\nHow are you?\nYour age is: " + age)
print("\n\n\n\n\n\n")
                                     #קריאת קלט מלקוח
name1=input("Enter your name: ")
age1=input("Enter your age: ")
mail=input("Enter your mail: ")
#print(mail)
#print(type(mail))
print("\nFull Name: " + name1 + "\nYour age is: " + age1 + "\nYour mail: " + mail)

                                    #המרות משתנים
#מספרים שלמים
print(int("1"))
#שברים
print(float(1))
#תווים
print(str(57.3))