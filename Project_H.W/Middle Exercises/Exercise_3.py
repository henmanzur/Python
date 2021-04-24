'''
####################
# Middle exercises #
####################

3. Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them.
           Hen Manzur = r u z n a M n e H
'''

# 3.
fname = input("\n3.\nEnter a First Name: ")
lname = input("Enter a Last Name: ")
print("\nYour first name: ' " + str(fname) + " ' " + "\nYour last name: ' " \
       + str(lname) + " ' \n-----------------------------")
print("Your first name in reverse and spaces : ' " + str(' '.join(fname[::-1])) + " ' " + "\nYour last name in reverse and spaces: ' " \
       + str(' '.join(lname[::-1])) + " ' ")

print("\nGood Bye.\n")
# b = ' '.join(lname[::-1] + fname[::-1])
# print(b)