'''
1.
Create a dictionary with 5 names & money
2.
then calculate sum the money of the first & last names and print it to the screen
3.
after, add a new name with the sum of the money you calculated before in the end,
4.
print the number of entries
5.
and check if "idan" is inside the dictionary
'''
import time

#1.
print("\nCreating Dictionary...")
time.sleep(3)
my_dict = {"hen":105000, "idan":240000, "stav":37000, "ofer":450000, "eti":120000}
print(my_dict)
print("Dictionary Created.")
#2.
print("\nCalculates the amount of money of the first and last name in the Dictionary...")
time.sleep(3)
summary = my_dict["hen"] + my_dict["eti"]
print("The summary is: " + str(summary))
#3.
print("\nAdds a new name with the summary of the money calculates...")
time.sleep(3)
my_dict.update({"kristina":summary})
#my_dict["kristina2"] = summary - עוד אפשרות להוסיף שם אך ורק במידה והוא לא קיים במילון
print(my_dict)
print("'Kristina' was added to the dictionary with the amount of money calculated.")
#4.
print("\nPrinting the Dictionary and the number of Entries of the Dictionary...")
time.sleep(2)
print("The Dictionary : " + str(my_dict))
print("The number of Entries is : " + str(len(my_dict)))
#5.
print("\nChecking if 'idan' is inside the Dictionary...")
time.sleep(2)
print("idan" in my_dict)