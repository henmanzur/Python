'''
####################
# Middle exercises #
####################

13. Write a Python program to sum all the items in a list.
'''

# 13.
list = [1,2,3,4,5,6,7]

sum = 0
for i in range(len(list)):
    sum=sum+list[i]

print(sum)