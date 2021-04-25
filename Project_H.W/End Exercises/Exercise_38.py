'''
####################
#  End exercises   #
####################

38. Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
'''

# x = int(input("enter a number: "))
# y = int(input("enter a number: "))
# sum = ((x + y) * (x + y) ^ 2)
# print(sum)

x, y = 4, 3
result = x * x + 2 * x * y + y * y
print("({} + {}) ^ 2) = {}".format(x, y, result))