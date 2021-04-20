############
#רשימות
############
#כמו מחרוזות
#מאחסנות בתוכן רצף של איברים(מחרוזות, מספרים, שברים וכו') במקום תווים
'''
#הכרזה על רשימה(יצירת רשימה)
my_list1 = []
my_list2 = list() # אופציה שניה

#בניית רשימה
my_list3 = [0, 1.0, '3', []]

#חיבור רשימות
my_list4 = my_list3 + [77]

# הכפלת רשימות
my_list5 = my_list4*2
'''
new_list = [2, 6.6, "hen manzur", []]
print(type(new_list))
print(new_list)
print(new_list[0]) # הדפסת תא ספציפי כאשר התא הראשון הוא תמיד 0

new_list2 = new_list + [77, 'hello world'] #הוספת תא לnew_list בעזרת חיבור באמצעות new_list2
print(new_list2)

new_list3 = new_list + new_list2
print(new_list3) # מדפיס את שני הרשימות ביחד

new_list4 = new_list2*2 # הכפלה של רשימה
print(new_list4)

'''
בניית רשימה עם לולאה (למתקדמים)
my_list6 = [i for i in my_list5]

בניית רשימה עם ללואה ותנאי (למתקדמים)
my_list7 = [i for i in my_list5 if isinstance(i, int)]

בניית רשימה ממחרוזת
my_list8 = list("123456")

בניית מחרוזת מרשימה
my_string1 = ''.join(my_list8)

המרת מחרוזת לרשימה
my_list9 = mystring1.split()

שימוש בLEN לתאר את גודל הרשימה
print(len(my_list1))

נשתמש בAPPEND בכדי להוסיף ערך לרשימה
my_list1.append(1)
my_list1.append(3)
my_list1.append(4)
my_list1.append(5)
print(len(my_list1))

נשתמש בINSERT אם נרצה להוסיף ערך לרשימה במקום מסויים
תמנעו מפעולה זו כיוון שהיא פוגעת בביצועים#
my_list1.insert(1, 2)
print(my_list1)

נשתמש בPOP בכדי להוציא ערך מהרשימה
pop1 = my_list1.pop(1)
תמיד כדאי להוציא/להוסיף ערך לסוף הרשימה כדי לא לפגוע בביצועים#
pop_last = my_list1.pop()
print(len(my_list1))
print(my)list1

נבדוק שערך קיים ברשימה #
print("google" in ["toornado, ocean, "huriccan", "google"])

פנייה לאיברים מתוך הרשימה #
print(pop1, pop_last, my_list1[0], my_list1[-1])
'''
#list()
my_list8 = list("1234567") # כל תו תופס תא ברשימה
print(my_list8)

#.join()
my_string = ''.join(my_list8) # (יעשה רווח בין כל תא ברשימה) בניית מחרוזת מרשימה
print(my_string)
my_string2 = 'A'.join(my_list8) # בניית מחרוזת מרשימה
print(my_string2)

#.split()
my_list9 = my_string.split() # מחבר את כל המחרוזת לתא אחד ברשימה כל עוד אין רווחים
print(my_list9) # במידה ויש רווחים במחרוזת split יצור תא לאחר כל רווח במחרוזת

#.splitlines()
my_string3 = "Hello Hen How are you"
my_list10 = my_string3.splitlines() # splitlines במידה ויש רווחים ונרצה לאחד את כל המחרוזת לתא אחד ברשימה
print(my_list10) #  כל עוד לא ירדה שורה באמצעות n\ במידה ויש ירדת שורה במחרוזת splitlines יצור תא לכל שורה

my_string4 = "Hello Hen \n How are you" # במקרה של ירידת שורה
my_list11 = my_string4.splitlines() # splitlines במידה ויש רווחים ונרצה לאחד את כל המחרוזת לתא אחד ברשימה
print(my_list11)

#len()
my_list12 = ["hello", 1, 66.6, "Hen"]
print(len(my_list12)) # len מציג את אורך הרשימה
print("The length of my_list12 is: " + str(len(my_list12))) # len מציג את אורך הרשימה
my_str = "1212121233333333333333333333"
print("The length of my_str is: " + str(len(my_str))) #len עובד על כל אובייקט ולא רק על רשימות

#.append()
my_list12.append("wow") # append מוסיף לסוף הרשימה עוד משתנה
my_list12.append("hen") # append מוסיף לסוף הרשימה עוד משתנה
print(my_list12)
print("The new length of my_list12 is: " + str(len(my_list12)))

#.insert()
my_list12.insert(3, "bla bla bla") #insert מוסיף ערך לאיזור ספציפי ברשימה ע"י דחיפה של התא שנמצא במיקום קדימה ברשימה
print(my_list12)

#.pop()
my_list12.pop() # pop מושך(מוציא) את התא האחרון ברשימה
print(my_list12)
my_list12.pop(3) # pop מושך(מוציא) את התא במיקום שנרשם בסוגריים
print(my_list12)

#in  - True/False
my_list13 = ["google", "facebook", "ebay", "apple"]
print("ebay" in my_list13) # מדפיס אם המחרוזת "ebay" נמצאת ברשימה (True/False)

