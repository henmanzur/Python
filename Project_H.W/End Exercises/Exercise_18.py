'''
####################
#  End exercises   #
####################

18. Write a Python program to calculate the sum of three given numbers, if
the values are equal then return three times of their sum.
'''

def sum_thrice(x, y, z):
    sum = x + y + z

    if(x == y == z):
        sum = sum * 3
    return sum

print('''
18.Python program to calculate the sum of three given numbers, if
the values are equal then return three times of their sum.
''')
print(sum_thrice(int(input("Enter 1st Number: ")), int(input("Enter 2nd Number: ")), int(input("Enter 3rd Number: "))))

