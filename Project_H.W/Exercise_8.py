'''
####################
# Middle exercises #
####################

8. Write a Python program to empty a variable without destroying it.
Sample data:
n=20
d = {"x":200}
Expected Output :
0
{}
'''
# 8.
n = 20
d = {"x":200}
l = [1,3,5]
# ברגע שרושמים בtype עוד סוגריים הוא מדפיס את משתנים ריקים אבל מאותו הסוג
print(type(n)())
print(type(d)())
print(type(l)())