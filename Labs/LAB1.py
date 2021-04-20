                        #####################################################
                        #                  - תרגיל LAB 1 -
                        #####################################################
num = int(input("Enter a number with 4 digits: "))
'''
#This is Alafim
print("Alafim = " + str(num//1000))

#This is Meot
print("Meot = " + str((num%1000)//100))

#This is Asarot
print("Asarot = " + str((num%100)//10))

#This is Ahadot
print("Ahadot = " + str(num%10))
'''

print("Alafim = " + str(num//1000) + "\nMeot = " + str((num%1000)//100) + "\nAsarot = " + str(((num%100)//10)) + "\nAhadot = " + str(num%10))
