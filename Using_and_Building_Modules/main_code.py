'''
from time import sleep  # מושך מסיפריית(module) time את פונקציית sleep
from time import sleep, clock  # מושך מסיפריית(module) time את הפונקציות clock ,sleep
from time import *  # מושך מסיפריית(module) את כל הפונקציית

#במידה ונמשוך את הספרייה עם פירוט איזה פונקציה נשתמש בפקודה כך על מנת להפעילה
sleep(3)

#########################################################################################

import time # מושך את כל ספריית(module) time
#במידה ונמשוך את הספרייה ללא פירוט איזה פונקציה נשתמש בפקודה כך על מנת להפעילה
time.sleep(3)


#########################################################################################

# יצרתי קובץ Functions_def שבו רשמתי פונקציות מסויימות

#from Functions_def import *
# לאחר מכן פתחתי הרשאה לשימוש בפונקציות על ידי הפקודה from Functions_def import

במידה והקובץ נמצא בתיקייה נרשום את המיקום המדוייק (full path) של הקובץ
לדוגמא:
from Using_and_Building_Modules.Functions_def import menu, calculating

במידה ורוצים למשוך פונקציה מסיפרייה שלא נמצאת באותו פרוייקט נציין גם את הפרוייקט לפני שם התיקייה
לדוגמא:
from Test_Project.Using_and_Building_Modules.Functions_def import menu, calculating

#########################################################################################

'''
from random import randint
from time import sleep
from Using_and_Building_Modules.Functions_def import menu, calculating, dogs_age


menu()
sleep(3)
print("wow\n")
calculating(3,6)
dogs_age(int(input("Enter dog's age: ")))
