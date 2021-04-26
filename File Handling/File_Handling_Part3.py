##########################
# File Handling - Part 3 #
##########################

# # יצירת רשימה מתוך קובץ גם אם בשורות נפרדות
# filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/File Handling/Files/hello.txt"
# file = open(filename, "r")
# new_list = [] # יצירת LIST ריק
# new_list = file.read().splitlines() # קורא ומפצל את כל השורות בקובץ
# print((type(new_list)))
# print(new_list)
# file.close()
# #####
# print(new_list) # מדפיס כל שורה בפני עצמה
# for i in new_list:
#     print(i)

filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/File Handling/Files/hello.txt"
file = open(filename, "r")
print(file.readlines()[2])  # על מנת להדפיס שורה מסויימת 0 = שורה ראשונה
# print(file.read()[0])  # על מנת להדפיס תו מסויים 0 = תו ראשון
# print(file.read(3))  # על מנת להדפיס את שלושת התווים הראשונים, 1 = תו ראשון
file.close()

#########################
##Create a empty file
# f = open("C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/File Handling/Files/hello5.txt", "x")
# f.close()

