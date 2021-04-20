'''
####################
# Middle exercises #
####################

3. Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them.
'''

# 3.
fname = input("\n3.\nEnter a First Name: ")
lname = input("Enter a Last Name: ")
print("\nYour first name in reverse ' " + str(fname[::-1]) + " ' " + "\nYour last name in reverse ' " \
      + str(lname[::-1]) + " ' ")