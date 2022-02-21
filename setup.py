import os
import time

with open('users/info.data', 'w') as f:
    f.writelines('1')

print("""

███████╗██╗░░░██╗░█████╗░██╗░░██╗░█████╗░░██████╗
██╔════╝██║░░░██║██╔══██╗██║░██╔╝██╔══██╗██╔════╝
█████╗░░██║░░░██║██║░░╚═╝█████═╝░██║░░██║╚█████╗░
██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░██║░░██║░╚═══██╗
██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗╚█████╔╝██████╔╝
╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░

░██████╗███████╗████████╗██╗░░░██╗██████╗░
██╔════╝██╔════╝╚══██╔══╝██║░░░██║██╔══██╗
╚█████╗░█████╗░░░░░██║░░░██║░░░██║██████╔╝
░╚═══██╗██╔══╝░░░░░██║░░░██║░░░██║██╔═══╝░
██████╔╝███████╗░░░██║░░░╚██████╔╝██║░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░
""")

name = input("Enter Your Username To Be Displayed: ")
pas = input("Enter Your Password To Login: ")

with open('users/dataname.pass', 'w') as f:
    f.writelines(name)

with open('users/password.pass', 'w') as f:
    f.writelines(pas)

print("Setup Complete!!!")
print("Opening Login Page...")
time.sleep(0.5)
os.startfile('login.py')