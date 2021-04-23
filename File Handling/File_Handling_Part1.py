'''
#‘r’ – Read mode which is used when the file is only being read
#‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated)
#‘a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end
#‘r+’ – Special read and write mode, which is used to handle both actions when working with a file

'''
'''
# r = read לקרוא קובץ

filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/File Handling/Files/hello.txt" # יצירת משתנה למיקום הקובץ
file = open(filename, "r") # יצירת משתנה לפקודה לפתיחת הקובץ עם הרשאת r(read)
print(file.read()) # הדפסה של משתנה file וקריאתו
file.close() # סגירת הקובץ(חובה לסגור קובץ לאחר כל פעולה על מנת לפתוח אותו בהרשאה אחרת)

################################################################################################################

# w = write כותב לקובץ ודורס את המידע שקיים בו

file = open(filename, "w")
file.write("192.168.1.1\n192.168.1.2") # פקודה זו תרשום בתוך הקובץ את מה שרשום בסוגריים
file.close()

################################################################################################################
# r+ = read and write כותב וקורא את הקובץ ( דורס את המידע הקיים בקובץ )

file = open(filename, "r+")
print(file.read())
file.write("192.168.1.5\n192.168.1.6") # פקודה זו תרשום בתוך הקובץ את מה שרשום בסוגריים
print(file.read())
file.close()

################################################################################################################

#a = append כותב לקובץ ולא דורס את המידע שקיים בו(מוסיף)

file = open(filename, "a")
file.write("192.168.1.3\n192.168.1.4") # פקודה זו תרשום בתוך הקובץ את מה שרשום בסוגריים
file.close()

#נוסיף קריאת קובץ באמצעות read לאחר הappend על מנת להציג לנו את הקובץ לאחר ההוספה של המידע באמצעות append(a)

file = open(filename, "r")
print(file.read())
file.close()

################################################################################################################

# a+ = read and append כותב וקורא את הקובץ ( מוסיף כתיבה לסוף הקובץ ולא דורס את המידע הקיים בקובץ )

file = open(filename, "a+")
print(file.read())
file.write("192.168.1.5\n192.168.1.6") # פקודה זו תרשום בתוך הקובץ את מה שרשום בסוגריים
print(file.read())
file.close()
'''