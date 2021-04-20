'''
Write a code that will show the menu:
Menu:
1.Insert Number and ** it by 3 (בחזקת 3)
2.Insert 4 IPs to a list and print it
3.Insert 4 Entries to DNS_Dictionary and print it
4.Check if a string is Palindrome (aba קריא מימין ומשמאל לדוגמא)

if the user won't choose 1-4, you will tell him to insert 1-4 only!!
'''

choise = input("\nMenu:\n-----\n1.Insert Number and ** it by 3\n2.Insert 4 IPs to a list and print it\n3.Insert 4 Entries to DNS_Dictionary and print it\n4.Check if a string is Palindrome\nChoose 1-4 from the menu: \n")

if(choise == "1"):
    CHOOSE1 = int(input("Insert Number: \n"))
    print("The summary of " + str(CHOOSE1) + "³ is: " + str(CHOOSE1**3))
elif(choise == "2"):
    list_ip = []
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    list_ip.append(input("Enter new IP: "))
    print("\nYour IPs list is:\n" + str(list_ip))
elif (choise == "3"):
    dns_dict={}
    dns_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter an IP: ")})
    print("\nThis is the new DNS Dictionary: \n" + str(dns_dict))
elif (choise == "4"):
    word = input("Enter a word: \n")
    if (word == word[::-1]):
        print("This is Palindrome!")
    else:
        print("This isn't Palindrome!")
else:
    print("Enter 1-4 only!!")

print("\nGood Bye.")