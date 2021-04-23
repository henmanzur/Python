##########################
# File Handling - Part 2 #
##########################

'''
filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/File Handling/Files/hello.txt" # יצירת משתנה למיקום הקובץ
file = open(filename, "r") # יצירת משתנה לפקודה לפתיחת הקובץ עם הרשאת r(read)
for line in file:  # יצירת לולאה עם משתנה line בתוך file( הקובץ שפתחנו ) על מנת לקרוא מתוך הקובץ כל שורה בפני עצמה
    print(line)
file.close() # סגירת הקובץ
'''

'''

filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/File Handling/Files/hello.txt" # יצירת משתנה למיקום הקובץ
file = open(filename, "r") # יצירת משתנה לפקודה לפתיחת הקובץ עם הרשאת r(read)
my_string = file.read() # הכנסת הפקודה file.read() למשתנה my_string
file.close() # סגירת הקובץ(חובה לסגור קובץ לאחר כל פעולה על מנת לפתוח אותו בהרשאה אחרת)
print(my_string) # כמו לרשום print(file.read()) הפקודה תדפיס את הקובץ
my_list = my_string.split(",") # .split() אומר לפצל את המחרוזת הרשומה בתוך הקובץ לפי מה שרשום בסוגריים
                               #ותכניס את הstring לתוך רשימה(list)
print(type(my_list))
print(my_list)
'''