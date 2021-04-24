'''
####################
# Middle exercises #
####################

1. Write a Python program to print the following string in a specific format
(see the output).
Sample String : "Net4U, is the best place…in the world" Output :
"Net4U, is the best place
 …in the world"

2. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

3. Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them.

4. Write a Python program to accept a filename from the user and print
the extension of that.
Sample filename : abc.java
Output : java

5. Write a Python program that accepts an integer (n) and computes the
value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615

6. Write a Python program to find whether a given number (accept from
the user) is even or odd, print out an appropriate message to the user.

7. Write a Python program to convert height (in feet and inches) to 7
centimeters.
4

8. Write a Python program to empty a variable without destroying it.
Sample data: n=20
d = {"x":200}
Expected Output : 0
{}

9. Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}

10. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'Net4U'
Expected output: {'N': 1, 'e': 1, 't': 2, '4': 1, 'U': 1}

11. Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

12. Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2

13. Write a Python program to sum all the items in a list.

14. Write a Python program to print a specified list after removing the 0th,
4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''
from datetime import datetime

# 1.
print("1.\nNet4U, is the best place...in the world")

# 2.
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("\n2.\nCurrent Time =", current_time)

# 3.
fname = input("\n3.\nEnter a First Name: ")
lname = input("Enter a Last Name: ")
print("\nYour first name in reverse ' " + str(fname[::-1]) + " ' " + "\nYour last name in reverse ' " \
      + str(lname[::-1]) + " ' ")

# 4.
filename = input("\n4.\nEnter a file name: ")
print(str(filename) + ".java")

# 5.
a = int(input("5.\nInput an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print(str(n1) + "+" + str(n2) + "+" + str(n3) + "\n = ")
print (n1+n2+n3)

# 6.
num = int(input("\nEnter a number: "))
if (num%2 == 0):
    print("\nThis number is even\n")
else:
    print("\nThis number is odd")
# 7.

# 8.
n = 20
d = {"x":200}
l = [1,3,5]
# ברגע שרושמים בtype עוד סוגריים הוא מדפיס את משתנים ריקים אבל מאותו הסוג
print(type(n)())
print(type(d)())
print(type(l)())

# 9.

# 10.

# 11.

# 12.

# 13.
list = [1,2,3,4,5,6,7]

sum = 0
for i in range(len(list)):
    sum=sum+list[i]

print(sum)

# 14.
list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list.pop(5)
list.pop(4)
list.pop(0)
print(list)