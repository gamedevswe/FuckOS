import webbrowser

print("""

███████╗██╗░░░██╗░█████╗░██╗░░██╗░█████╗░░██████╗░░░░░░███████╗███╗░░██╗░██████╗░██╗███╗░░██╗███████╗
██╔════╝██║░░░██║██╔══██╗██║░██╔╝██╔══██╗██╔════╝░░░░░░██╔════╝████╗░██║██╔════╝░██║████╗░██║██╔════╝
█████╗░░██║░░░██║██║░░╚═╝█████═╝░██║░░██║╚█████╗░█████╗█████╗░░██╔██╗██║██║░░██╗░██║██╔██╗██║█████╗░░
██╔══╝░░██║░░░██║██║░░██╗██╔═██╗░██║░░██║░╚═══██╗╚════╝██╔══╝░░██║╚████║██║░░╚██╗██║██║╚████║██╔══╝░░
██║░░░░░╚██████╔╝╚█████╔╝██║░╚██╗╚█████╔╝██████╔╝░░░░░░███████╗██║░╚███║╚██████╔╝██║██║░╚███║███████╗
╚═╝░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░░░░╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝░░╚══╝╚══════╝
""")

while True:
    browse = input("Search browser or type URL: ")
    webbrowser.open(browse)