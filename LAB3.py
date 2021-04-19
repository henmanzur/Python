'''
1.Create 2 variables : string of your full name, another string of your mail.
Create variable of your age (integer)
print all of them to the screen

2.then Print your name from the end to beginning and print it only with your age*3

3.then cehck if your name is stored inside this full string
"hen idan ben dudu shimon yael adam shahar kristina hai"
'''
#1)
full_name = "hen manzur"
mail = "henmanzur@gmail.com"
age = 27
print("1.\nFull Name: " + full_name + "\nAge: " + str(age) + "\nEmail: " + mail)
#2)
print("\n2.\nFull name: " + full_name[::-1] + "\nAge: " + str(age*3))
#3)
names = '''
hen idan ben dudu shimon yael adam shahar kristina hai
'''
print("\n3.")
print("hen" in names)