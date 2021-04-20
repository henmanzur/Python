'''
כתיבת תוכנית אשר תקבל סל קניות מבחוץ ותחשב מה העלות שלו :
עגבנייה - 3 ש"ח
מלפפון - 2 ש"ח
קולה - 5 ש"ח
עוף - 20 ש"ח לק"ג
התוכנית תחשב את המחיר לתלשום לפני ואחרי מע"מ ( 17% ), ללא שארית.
'''
print("Now we will calculate your marketing:\nPrices:\n---------\nTomato = 3NIS\nCucumber = 2NIS\nCola = 5NIS\nChicken = 20NIS\n")
tomatos = int(input("Enter how many Tomatos: "))
cucumbers = int(input("Enter how many Cucumber: "))
colas = int(input("Enter how many Colas: "))
chickens = int(input("Enter how many Chickens: "))

print("\nSummary of your order:\n---------\nTomatos: " + str(tomatos) + "\nCucumbers: " + str(cucumbers) + "\nColas: " + str(colas) + "\nChickens: " + str(chickens))
# sum1 = tomatos * 3
# sum2 = cucumbers * 2
# sum3 = colas * 5
# sum4 = chickens * 20
summary = (tomatos * 3) + (cucumbers * 2) + (colas * 5) + (chickens * 20)
# summaryvat = (tomatos * 3) + (cucumbers * 2) + (colas * 5) + (chickens * 20) * 1.17

print("\nYou have to pay: " + str(summary) + " NIS without VAT.")
print("You have to pay: " + str("%.2f" % (summary*1.17)) + " NIS with 17% VAT.")
# "%.2f" - 2 floats