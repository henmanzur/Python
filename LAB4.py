'''
1.
Create a list with 4 details about you: name, age, mail, phone number and print it to screen
2.
then Create another list with 2 IPs,
3.
then add 3 more IPs, pop the 3rd IP and print how many
IPs do we have and print them
'''

details_list = ["Hen Manzur", 27, "henmanzur@gmail.com", "052-4710148"]
print("\nFull name: " + str(details_list[0]) + "\nAge: " + str(details_list[1]) + "\nEmail: " + str(details_list[2]) +"\nPhone Number: " + str(details_list[3] + "\n"))

ips_list = ["192.168.1.2", "10.1.2.0"]
ips_list.append("127.0.0.1")
ips_list.append("127.0.0.2")
ips_list.append("127.0.0.3")
print(ips_list)
ips_list.pop(2)
print(ips_list)
print("The length of the new IPs list is: " + str(len(ips_list)))