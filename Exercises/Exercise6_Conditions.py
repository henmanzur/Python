################
#  Conditions  #
###############
'''
# Python Comparison Operators רשימה של כל סוגי ההשוואות
== equal to
!= not equal
<> similar to !=
> greater then
> smaller then
>= greater then or equal to
<= smaller then or equal to

סוגי השוואות נוספות :
not
in
is
and
or
'''
#דוגמא 1
# NAME = input("Enter a name: ")
# if(NAME == "Hen"):
#     print("Hello Hen\n")
#     AGE = int(input("Enter a Age: "))
#     if(AGE == 27):
#         print("Wow you are 27 years old")
#     else:
#         print("you are too young")
# else:
#     print("Where is Hen?\n")

# דוגמא 2
# number = int(input("Enter a number: \n"))
# if(number == 6):
#     print(number*2)
# else:
#     print(number-1)
# דוגמא 3
# number = int(input("Enter a number: \n"))
# if(number > 6):
#     print(number*2)
# else:
#     print(number-1)

 # דוגמא and,or .4
name = input("Enter you name: \n")
age = int(input("Enter your age: \n"))
if ((name == "hen" or name == "Hen") and (age>=18)):
    print("You can enter to the Club!")
else:
    print("You are not allowed to enter...")
