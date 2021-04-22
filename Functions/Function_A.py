###############
# Functions A #
###############

'''
################################################################################################################
################################################################################################################

הפונקציות מתחלקות ל4 חלקים

1. ##############################################################################################################
                                                      1
פונקציות ששלא מקבלות ערך ולא מחזירות ערך
לדוגמה:

def calculating():  #  ברגע שלא מכניסים ערך לסוגריים של הפונקציה זו פונקציה שלא מקבלת ערך וכשקוראים לה היא לא מצפה לקבל שום ערך
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    print("Your new number is: " + str(num1*num2))

calculating()

2. ##############################################################################################################
                                                      2
                                  פונקציות שלא מקבלות ערך אבל כן מחזירות ערך
לדוגמה:

def calculating2():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    sum = num1*num2
    print("Your new number is: " + str(sum))
    return sum

a = calculating2() + 29
print("WOW: " + str(a))

3. ##############################################################################################################
                                                      3
                                   פונקציות שכן מקבלות ערך וכן מחזירות ערך
                                                    לדוגמה:

def calculating3(x,y):
    print("Your first number: " + str(x) + "\nYour second number: " + str(y))
    sum = x**y
    print("\nYour new number is: " + str(sum))
    return sum

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
hen = calculating3(a,b) + 29
print("WOW: " + str(hen))

                                                    דוגמה 2:
def add_ip(ip1,ip2,ip3):
    list=[]
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list


ip_list=[]
ip_n1=input("Enter first IP: ")
ip_n2=input("Enter 2nd IP: ")
ip_n3=input("Enter 3rd IP: ")
ip_list=add_ip(ip_n1,ip_n2,ip_n3)
ip_list=add_ip(ip_n1,ip_n2,ip_n3)
print(ip_list)

4. ##############################################################################################################
                                                      4
                                     פונקציות שכן מקבלות ערך ולא מחזירות ערך
לדוגמה:


def calculating4(x,y):  # לא משנה מה int float string שהם יכולים להיות  (x וy) פונקציה זו כן מצפה לקבל ערך
    print("Your first number: " + str(x) + "\nYour second number: " + str(y))

calculating4(1,2)  # ידפיס למסך מספר ראשון 1 מספר שני 2 x=1 y=2


##############################################################
##############################################################
פונקציות הן קטע קוד שרץ כשקוראים לו

def my_function():   #### ככה נרשמת פונקציה def
    print("Hello Function") #### הקוד שבפונקציה

my_function()  ##### קריאה לפונקציה
#############################################################
                ניתן להעביר לפונקציה פרמטרים

def my_function(name):
    print(name + `net`)

my_function("dog")
my_function("bog")
my_function("zog")
#############################################################
פונקציות יכולות להחזיר פרמטרים
def my_function(x):
    return x*x

print(my_function(1))
print(my_function(1))
#############################################################
פונקציות יכולות לקבל פרמטרים דיפולטיביים
def my_function(name="Hen"):
    print(name + ".net")

my function("boss")
my function()
#############################################################
פונקציות יכולות לקבל מספר פרמטרים
def my_function(service,name="Hen"):
    print(service + ':' + name " ".net"

my_function("ping","boss")
my_function("ssh")
'''

def Market(): # ככה נרשמת פונקציה
    print("Now we will calculate your marketing:\nPrices:\n---------\nTomato = 3NIS\nCucumber = 2NIS\nCola = 5NIS\nChicken = 20NIS\n")
    tomatos = int(input("Enter how many Tomatos: "))
    cucumbers = int(input("Enter how many Cucumber: "))
    colas = int(input("Enter how many Colas: "))
    chickens = int(input("Enter how many Chickens: "))

    print("\nSummary of your order:\n---------\nTomatos: " + str(tomatos) + "\nCucumbers: " + str(cucumbers) + "\nColas: " + str(colas) + "\nChickens: " + str(chickens))

    summary = (tomatos * 3) + (cucumbers * 2) + (colas * 5) + (chickens * 20)
    print("\nYou have to pay: " + str(summary) + " NIS without VAT.")
    print("You have to pay: " + str("%.2f" % (summary*1.17)) + " NIS with 17% VAT.")
    # "%.2f" - 2 floats

for i in range(10):
    Market()