'''
####################
#  End exercises   #
####################

34. Write a Python program to sum of two given integers. However, if the sum
is between 15 to 20 it will return 20.
'''

def Exercise_34(x, y):
    # x = int(input("Enter 1st number: "))
    # print("       +")
    # y = int(input("Enter 2nd number: "))
    sum = x + y

    #if sum in range(15, 20): ## עוד אפשרות
        #return 20
    #else:
        #return sum
    if x + y >= 15 and x + y <=20 :
        print("       =\nthe sum is between 15 to 20 it will return '20'")
    else:
        print("       =\nthe sum is not between 14 to 20: " + str(sum))
    return sum

Exercise_34(10,6)

'''
def Exercise_34():
    x = int(input("Enter 1st number: "))
    print("       +")
    y = int(input("Enter 2nd number: "))
    sum = x + y

    if x + y >= 15 and x + y <=20 :
        print("       =\nthe sum is between 15 to 20 it will return '20'")
    else:
        print("       =\nthe sum is not between 14 to 20: " + str(sum))
    

Exercise_34()
'''