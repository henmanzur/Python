'''
####################
# Middle exercises #
####################

14. Write a Python program to print a specified list after removing the 0th,
4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''
# 14.
list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list.pop(5)
list.pop(4)
list.pop(0)
print(list)