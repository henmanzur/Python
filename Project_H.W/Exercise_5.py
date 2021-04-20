'''
####################
# Middle exercises #
####################

Write a Python program that accepts an integer (n) and computes the
value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''
# 5.
a = int(input("5.\nInput an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print(str(n1) + "+" + str(n2) + "+" + str(n3) + "\n = ")
print (n1+n2+n3)