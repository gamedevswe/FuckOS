import time
import os
import socket

login_pass = open('users/password.pass')
login_name = open('users/dataname.pass')
l_p = login_pass.read()
l_n = login_name.read()

print("""

███████╗██╗░░░██╗░█████╗░██╗░░██╗░█████╗░░██████╗
██╔════╝██║░░░██║██╔══██╗██║░██╔╝██╔══██╗██╔════╝
█████╗░░██║░░░██║██║░░╚═╝█████═╝░██║░░██║╚█████╗░
██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░██║░░██║░╚═══██╗
██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗╚█████╔╝██████╔╝
╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░
""")

print("Welcome " + l_n + "!")
print("The date is: " + time.strftime("%m/%d/%y"))
print("""
[1] To Open Google
[2] To Open Text Editor
[3] To Open File Explorer
[4] To Configure And Open BioS
[5] To Open Terminal
[6] To Open Open Calculator
[7] To Close OS Safley
""")

select = input("[?]: ")

if select == '1':
    os.startfile('brows.py')
    os.startfile(r'C:\Users\Hugo\Desktop\projects\OperatingSystems\FuckOS\home.py')
    os.system('exit')

if select == '2':
    os.startfile('edit.py')
    os.startfile(r'C:\Users\Hugo\Desktop\projects\OperatingSystems\FuckOS\home.py')
    os.system('exit')

if select == '3':
    os.startfile('open.py')
    os.startfile(r'C:\Users\Hugo\Desktop\projects\OperatingSystems\FuckOS\home.py')
    os.system('exit')

if select == '4':
    while True:
        b_login = input(str("Enter The Password To " + l_n + " To Open BioS: "))

        if b_login == l_p:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            print("[1] Username: " + l_n)
            print("[2] Password: " + l_p)
            print("Hostname: ", host_name)
            print("Local IPS: " + host_ip)
            edit_b = input("[?]: ")

            if edit_b == '1':
                edit_n = input("Enter New Username: ")
                with open('users/dataname.pass', 'w') as f:
                    f.writelines(edit_n)
                print("Username Changed To " + edit_n)
                print("Press Enter To Restart: ")
                os.startfile(r'C:\Users\Hugo\Desktop\projects\OperatingSystems\FuckOS\home.py')
                os.system('exit')

            if edit_b == '2':
                edit_p = input("Enter New Password: ")
                with open('users/password.pass', 'w') as f:
                    f.writelines(edit_p)
                print("Password Changed To " + edit_p)
                print("Press Enter To Restart: ")
                os.startfile(r"C:\Users\Hugo\Desktop\projects\OperatingSystems\FuckOS\home.py")
                os.system('exit')

if select == '5':
    os.startfile('terminal.py')
    os.startfile(r'C:\Users\Hugo\Desktop\projects\OperatingSystems\FuckOS\home.py')
    os.system('exit')

if select == '6':
    os.startfile('calc.py')
    os.startfile(r'C:\Users\Hugo\Desktop\projects\OperatingSystems\FuckOS\home.py')
    os.system('exit')

if select == '7':
    os.system('exit')