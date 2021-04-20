'''
####################
# Middle exercises #
####################

2. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
'''
from datetime import datetime
# 2.
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("\n2.\nCurrent Time =", current_time)
