'''
####################
#  End exercises   #
####################

149. Write a Python function that takes a positive integer and returns the sum
of the cube(בשלישית,בחזקת 3) of all the positive(חיובי, גדול מ0) integers smaller than the specified number.
Example:
num = 5
sum = 1**3 2**3 3**3 4**3
'''

# def positive(num):
#     sum=0
#     for i in range(1,num):
#         sum=sum+(i**3)
#     print("The Summary is: " + str(sum))
#     return sum
#
# new_sum=positive(int(input("Enter a positive number: ")))

def sum_of_cubes(n):
  n = n-1
  total = 0
  while n > 0:
    total =total+( n * n * n)
    n = n-1
  return total

print("Sum of cubes: " + str(sum_of_cubes(3)))