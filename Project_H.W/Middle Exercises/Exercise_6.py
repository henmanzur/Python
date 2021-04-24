'''
####################
# Middle exercises #
####################

6. Write a Python program to find whether a given number (accept from
the user) is even or odd, print out an appropriate message to the user.
יצירת תוכנה הקולטת מספר מהמשתמש ובודקת אם המספר זוגי או אי זוגי
'''
# 6.
num = int(input("\nEnter a number: "))
if (num%2 == 0):
    print("\nThis number is even\n")
else:
    print("\nThis number is odd")