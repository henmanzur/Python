'''
Create a menu:
a. IP System?
b. DNS System?

a ### כל כתובות האייפי יהיו בקובץ טקסט נפרד
====
    1. search for IP address from a list
    2. add IP address to a list
    3. Delete IP address to a list
    4. Print all the IPs to the screen

b
====
    1. search for URL from a dictionary
    2. add URL + IP address to a dictionary
    3. Delete URL from a dictionary
    4. Update the IP address of specific URL
    5. Print all the URL:IP to the screen

            כל הפונקציות יהיו בקובץ פייטון LAB10_Functions.py ונמשוך אותם משם לקובץ LAB10.py
'''

##############################################  -  Python Module File  -  #######################################################
from time import sleep
import os

#######################################################  -  MAIN MENU  -  #######################################################

def Main_Menu():

    while True:
        choise = input("\nMenu:\n-----\na. IP System?\nb. DNS System?\nc. Files System?\nEnter your Choise: ")
        if choise == "a" or choise == "A":
            IP_Menu()
        elif choise == "b" or choise == "B":
            DNS_Menu()
        elif choise == "c" or choise == "C":
            file_menu()
        else:
            print("\nEnter 'A', 'B' or 'C' only ! ❌\n-------------------------------")

        exit_main_menu = input("Do you want exit the Main Menu? y/n \n")
        if (exit_main_menu == "y" or exit_main_menu == "Y" or exit_main_menu == "yes" or exit_main_menu == "YES"):
            break
        else:
            print("\n-------------------\nWelcome Back! 👋")

    print("\nGood Bye.")


#######################################################  -  IP System Menu  -  #######################################################

def search_ip():
    search_ip = input("Enter IP to search in LAB10_IPs.txt: ")
    print("\nSearching...\n")
    sleep(3)

    filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/Labs/Lab10/IP_System/LAB10_IPs.txt"
    file = open(filename, "r")
    data = file.read()

    if (search_ip in data):
        print(str(search_ip) + " is exists in the file LAB10_IPs.txt! ✅ \n")
        print("Printing all IPs in LAB10_IPs.txt...\n")
        sleep(3)
        print("---------------------------\nAll IPs in LAB10_IPs.txt:\n" + data + "\n---------------------------")
    else:
        print(str(search_ip) + " is not exists. ✅\n")
        print("Printing all IPs in LAB10_IPs.txt...\n")
        sleep(3)
        print("---------------------------\nAll IPs in LAB10_IPs.txt:\n" + data + "\n---------------------------")
    file.close()

def add_ip():
    new_ip = input("Enter a new IP to append to LAB10_IPs.txt: ")
    print("---------------------------\nAppends the new IP...")
    sleep(3)
    filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/Labs/Lab10/IP_System/LAB10_IPs.txt"
    file = open(filename, "r")
    data = file.read()

    if (new_ip in data):
        print("\nThe IP '" + str(new_ip) + "' is already in use! ❌ \n---------------------------\n")
        file = open(filename, "r")
        print("Printing all the IPs in LAB10_IPs.txt...")
        sleep(3)
    else:
        filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/Labs/Lab10/IP_System/LAB10_IPs.txt"
        file = open(filename, "a")
        print(str(new_ip) + " is Added to the file LAB10_IPs.txt\n---------------------------\n")
        file.write("\n" + new_ip)
    file.close()

def delete_ip():
    ip_delete = input("Enter the IP Address to delete: ")
    filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/Labs/Lab10/IP_System/LAB10_IPs.txt"
    file = open(filename, "r")
    data = file.read()

    if ip_delete in data:
        print("\nDeleting the IP '" + ip_delete + "'...")
        sleep(3)
        print("\nThe IP '" + str(ip_delete) + "' Deleted.\n-------------------------------\nDone. ✅")
    else:
        print(ip_delete + " is not exists. ❌")

    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as file:
        for line in lines:
            if line.strip("\n") != ip_delete:
                file.write(line)
    file.close()

def print_ips():

    filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/Labs/Lab10/IP_System/LAB10_IPs.txt"
    file = open(filename, "r")
    data = file.read()
    print("\nOpening the file LAB10.txt...\n")
    sleep(2)
    print("Printing all IPs in LAB10_IPs.txt...\n")
    sleep(3)
    print("---------------------------\nAll IPs in LAB10_IPs.txt:\n" + data + "\n---------------------------")
    print("\nClosing the file LAB10.txt...\n")
    sleep(2)
    print("File Closed.")
    print("\n---------------------------\nDone.✅")

    file.close()

def IP_Menu():
    while True:
        ip_choise = input(
'''
IP System Menu:
---------------
1. search for IP address from a list
2. add IP address to a list
3. Delete IP address to a list
4. Print all the IPs to the screen
5. Get back to the MAIN MENU
        
Enter your Choise: ''')

        if ip_choise == "1":
            search_ip()
        elif ip_choise == "2":
            add_ip()
        elif ip_choise == "3":
            delete_ip()
        elif ip_choise == "4":
            print_ips()
        elif ip_choise == "5":
            print("\n-------------------\nWelcome Back! 👋")
            Main_Menu()
        else:
            print("\nEnter 1-5 only ! ❌\n-------------------")

        exit_ip_menu = input("\nDo you want exit? y/n \n")
        if (exit_ip_menu == "y" or exit_ip_menu == "Y" or exit_ip_menu == "yes" or exit_ip_menu == "YES"):
            print("\nGood Bye.")
            exit()
        else:
            print("\n-------------------\nWelcome Back! 👋")



#######################################################  -  DNS System Menu  -  #######################################################

dict_list = {"www.google.com":"1.1.1.1", "www.facebook.com":"2.2.2.2", "www.groo.co.il":"88.88.88.88", "www.youtube.com":"3.3.3.3"}

def search_url():
    search_url_dict = input("Enter URL to search: ")
    print("\nSearching URL in Dictionary...")
    sleep(3)
    if search_url_dict in dict_list :
        print("\n" + str(search_url_dict) + " is exists in the Dictionary.\n")
        print("Dictionary: " + str(dict_list) + "\n------------------------------------------------------------------------------------------------------------------------------\nDone. ✅")
    else:
        print("\n" + str(search_url_dict) + " is not exists in the Dictionary\n----------------------------------------------\nDone. ✅")


def add_url_ip():
    add_url_dict = input("Enter URL to add: ")
    add_ip_dict = input("Enter IP Address to add: ")

    if (add_url_dict in dict_list or add_ip_dict in dict_list.values()):
        print("\nURL: '" + str(add_url_dict) + "' and IP: '" + str(add_ip_dict) + "' is exists in the Dictionary ❌\n----------------------------------------------------------------\n")
    else:
        print("\nAdds a new URL and IP to the dictionary...")
        sleep(3)
        dict_list.update({str(add_url_dict) : str(add_ip_dict)})
        print("The new URL and IP Address have been added to the dictionary. ✅\n")
        print("Printing the new dictionary...\n")
        sleep(3)
        print("The new dictionary after the update:\n" + str(dict_list))
        print("\n-----------------------------------------------------------------\nDone. ✅ ")

def delete_url():
    delete_url_dict = input("Enter URL: ")

    if delete_url_dict in dict_list:
        del dict_list[str(delete_url_dict)]
        print("\nDeleting URL from Dictionary...")
        sleep(3)
        print(str(delete_url_dict) + " deleted. ✅\n--------------------------------\nDone. ✅ \n")
    else:
        print("\n" + str(delete_url_dict) + " is not exists in the Dictionary. ❌\n--------------------------------\n")

def update_ip_dict():
    update_ip_dict_url = input("Enter specific URL: ")
    update_ip_dict1 = input("Enter a new IP address: ")

    if (update_ip_dict_url in dict_list):
        print("\nUpdates the IP address to " + str(update_ip_dict_url) + "...\n")
        sleep(3)
        dict_list.update({str(update_ip_dict_url):str(update_ip_dict1)})
        print(str(update_ip_dict_url) + " has been updated with the new IP address: ")
        print({update_ip_dict_url : update_ip_dict1})
        print("-----------------------------------------------------------------\nDone. ✅ ")
    else:
        print("\n" + str(update_ip_dict_url) + " is not exists in the Dictionary. ❌\n------------------------------------------\n")

def print_dict():
    print("\nPrinting all the URL:IP to the screen...")
    sleep(3)
    print("\nAll Dictionary: " + str(dict_list))
    print("\n----------------------------------------------\nDone. ✅ ")

def DNS_Menu():

    while True:
        dns_choise = input(
'''
DNS System Menu:
---------------
1. search for URL from a dictionary
2. add URL + IP address to a dictionary
3. Delete URL from a dictionary
4. Update the IP address of specific URL
5. Print all the URL:IP to the screen
6. Get back to the MAIN MENU

Enter your Choise: ''')
        if dns_choise == "1":
            search_url()
        elif dns_choise == "2":
            add_url_ip()
        elif dns_choise == "3":
            delete_url()
        elif dns_choise == "4":
            update_ip_dict()
        elif dns_choise == "5":
            print_dict()
        elif dns_choise == "6":
            print("\n-------------------\nWelcome Back! 👋")
            Main_Menu()
        else:
            print("\n\nEnter 1-6 only ! ❌\n-------------------")

        exit_dns_menu = input("\nDo you want exit? y/n \n")
        if (exit_dns_menu == "y" or exit_dns_menu == "Y" or exit_dns_menu == "yes" or exit_dns_menu == "YES"):
            print("\nGood Bye.")
            exit()
        else:
            print("\n-------------------\nWelcome Back! 👋")


#######################################################  -  Files System Menu  -  #######################################################

def delete_file(file):
    filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/Labs/Lab10/File_System/" + file + ".txt"
    if os.path.exists(filename):
        os.remove(filename)
        print("\nFile Deleted.✔")
    else:
        print("\nThe file does not exist")

def create_file(file):
    f = open("C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/Labs/Lab10/File_System/" + file + ".txt" , "x")
    f.close()
    print("\nFile Created. ✔")
def read_file(file):
    filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/Labs/Lab10/File_System/" + file + ".txt"
    file = open(filename, "r")
    print("\n" + file.read() + "\n----------------------\nDone. ✔")
    file.close()

def write_file(file):
    filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/Labs/Lab10/File_System/" + file + ".txt"
    file = open(filename, "w")
    file.write(input("Enter IP: ") + "\n" + input("Enter IP: "))
    file.close()
    print("The IP addresses were successfully registered. ✔")

def append_file(file):
    filename = "C:/Users/Hen-PC/Desktop/Networking Course/Python/pythonProject/Python_Net4U_/Labs/Lab10/File_System/" + file + ".txt"
    file = open(filename, "a")
    file.write("\n" + input("Enter IP: ") + "\n" + input("Enter IP: "))
    file.close()
    print("The IP addresses were successfully appended. ✔")
def file_menu():

    while True:
        file_choise = input(
'''
Files System Menu:
---------------
1. Create a file
2. Read a file
3. Write to a file
4. Append to a file
5. Delete a file
6. Get back to the MAIN MENU
        
Enter your Choise: ''')
        if file_choise == "1":
            create_file(input("Enter file name: "))
        elif file_choise == "2":
            read_file(input("Enter file name: "))
        elif file_choise == "3":
            write_file(input("Enter file name: "))
        elif file_choise == "4":
            append_file(input("Enter file name: "))
        elif file_choise == "5":
            delete_file(input("Enter file name: "))
        elif file_choise == "6":
            print("\n-------------------\nWelcome Back! 👋")
            Main_Menu()
        else:
            print("\n\nEnter 1-6 only ! ❌\n-------------------")

        exit_file_menu = input("\nDo you want exit? y/n \n")
        if (exit_file_menu == "y" or exit_file_menu == "Y" or exit_file_menu == "yes" or exit_file_menu == "YES"):
            print("\nGood Bye.")
            exit()
        else:
            print("\n-------------------\nWelcome Back! 👋")

#######################################################  -  END  -  #######################################################