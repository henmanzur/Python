#######################
# מילונים Dictionary
#######################
'''
כמו רשימות
חיבור בין שם לערך ואחסון של זוגות שם:ערך
בדומה ספר טלפונים או רשימת כתובות מגורים עם שם ומספר
מתוארים גם כMAP וHASH TABLE

מילון(Dictionary) בנוי מ key: value
 key       value    key     value   key      value
למשל שם וגיל    idan manzur: 30, stav manzur: 18, hen manzur: 27


הכרזה על מילון #
my_dict1 = {}
mydict2 = dict()

בניית מילון #
my_dict3 = {'int': 0, 'float': 1.0, 'str: '3', 'list': []}
my_dict4 = dict(im='optimus', hen='mustard')

חיבור מילון #
my_dict5 = dict(my_dict3, **{'cool_number': 77})
my_dict6 = my_dict5.update(my_dict4)

שימוש בLEN לתאר את גודל המילון #
print(len(my_dict1))

הוספת שם:ערך למילון #
my_dict1['adi'] = '052-8507700'
my_dict1['nissan'] = '052-8507701'
my_dict1['bar'] = '052-8507702'
my_dict1['bob'] = '052-8507703'

מחיקת שם:ערך מהמילון #
del my_dict1['adi']

בדיקה ששם קיים במילון #
print("adi" in my_dict1)

נבדוק שערך קיים במילון #
print("052-8507700" in my_dict1.values())

פנייה לאיברים מתוך המילון #
print(my_dict1["bob"], my_dict1['adi'])

'''
#Dictionary דוגמאות
#במידה ויש 2 ערכים לkey נכניס אותם לlist
my_dict = {"www.google.com":"8.8.8.8","www.facebook.com":"7.7.7.7", "www.youtube.com":["5.5.5.5","4.4.4.4"]}
#my_dict.update({"www.net4u.com":"33.33.33.33", "www.groo.co.il":"88.88.88.88"}) # .update({key:value}) על מנת להוסיף למילון קיים

#.update(variable) עוד אפשרות להוספה למילון קיים
my_dict2 = {"www.net4u.com":"33.33.33.33", "www.groo.co.il":"88.88.88.88"}
print("my_dict: " + str(my_dict) + "\n")
print("my_dict2: " + str(my_dict2) + "\n")
my_dict.update(my_dict2)
print("my_dict.update: " + str(my_dict))
print("\nNumber of Entries: " + str(len(my_dict))) # אורך הרשימות בתוך המילון

#הדפסת value
print(my_dict["www.google.com"]) # ידפיס את הvalue של google
#print(my_dict.values()) # ידפיס את כל הערכים(values)

#עדכון value של key מסויים
my_dict["www.google.com"] = "8.8.4.4" # שינוי ערך לשם
print(my_dict["www.google.com"])

# בדיקה אם קיים שם בתוך מילון
print("www.google.com" in my_dict) #True = קיים | False = לא קיים
#בדיקה אם קיים ערך בתוך מילון
print("8.8.4.4" in my_dict.values()) #True = קיים | False = לא קיים
