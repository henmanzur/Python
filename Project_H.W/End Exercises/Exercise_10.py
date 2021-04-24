'''
####################
#  End exercises   #
####################

10. Write a Python program that accepts an integer (n) and computes the
value of n+nn+nnn
Sample value of n is 5
Expected Result : 615
Examples :
5+55+555
9+9+999
'''

n=int(input("Enter a number 1-9: "))
print(n + (n*10+n) + (n*100+n*10+n))

#n = 5
#n*10+n = 5*10+5 = 55
#n*100+n*10+n = 5*100+5*10+5 = 505+50 = 555