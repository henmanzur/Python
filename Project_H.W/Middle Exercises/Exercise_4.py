'''
####################
# Middle exercises #
####################

4. Write a Python program to accept a filename from the user and print
the extension of that.
Sample filename : abc.java
Output : java
'''
# 4.
filename = input("\n4.\nEnter the file name and extension: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
