'''
####################
#### Exercise 1 ####
####################

1. Create a code that will ask for your marketing budget.
 Facebook campaign = 100ILS per day.
 Instagram campaign = 50ILS per day.
Ask him:
How long he wants the Facebook campaign will run.
How long he wants the Instagram campaign will run.
Then print to the screen the summary of the cost in ILS with tax (17%)
If it is more than his marketing budget, tell him how much to add, if not tell him "successfull".
'''
from time import sleep

print("\n-------------------------------\nWelcome to my Marketing Project!\n")
print("Facebook Campaign cost 100ILS per day\nInstagram Campaign cost 50ILS per day\n-------------------------------")
sleep(1)
budget = int(input("\nEnter a your marketing budget: "))
faceCamp = int(input("How much days you want the Facebook Campaign will run: "))
instaCamp = int(input("How much days you want the Instagram Campaign will run: "))
print("\n-------------------------------")
facebook = 100
faceSum = faceCamp * facebook
faceTax = 0.17 * faceSum
faceTotal = faceSum + faceTax
faceMore = faceTotal - budget
faceChange = budget - faceTotal

instagram = 50
instaSum = instaCamp * instagram
instaTax = 0.17 * instaSum
instaTotal = instaSum + instaTax
instaMore = instaTotal - budget
instaChange = budget - instaTotal

print("\nThe summary of the cost in ILS with tax (17%) for the Facebook Campaign is : " + str(faceTotal))
print("The summary of the cost in ILS with tax (17%) for the Instagram Campaign is : " + str(instaTotal) + "\n\n-------------------------------\n")

if(budget>=faceTotal):
    print("Facebook: successfull and your change is: " + str(faceChange) + "ILS")
else:
    print("Facebook: You don't have enough money for the Facebook Campaign you need more " + str(faceMore) + "ILS")

if(budget>=instaTotal):
    print("Instagram: successfull and your change is: " + str(instaChange) + "\n-------------------------------")
else:
    print("Instagram: You don't have enough money for the Instagram Campaign you need more " + str(instaMore) + "ILS\n\n-------------------------------")

print("\nGood Bye.\n")