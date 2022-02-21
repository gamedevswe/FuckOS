import os
import time

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

██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
""")

while True:
    log = input("Enter Password To " + l_n + " To Login: ")

    if log == l_p:
        print("Opening Home Page...")
        time.sleep(0.5)
        os.startfile(r'C:\Users\Hugo\Desktop\projects\OperatingSystems\FuckOS\home.py')
        break

    else:
        print("Wrong Password To " + l_n)