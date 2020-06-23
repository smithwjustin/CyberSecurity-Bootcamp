


import os, sys


def main():
    
    
    if os.path.exists("CyberSecurity-Notes"):
        print("There is already folder with this name! ")
        sys.exit()
    
    else:
        os.mkdir("CyberSecurity-Notes")
    
    
    for j in range(1, 25):
        os.mkdir("Cybersecurity-Notes/Week {}".format(j))
    
        for s in range (1, 4):
            os.mkdir("Cybersecurity-Notes/Week {}/Day {}".format(j, s))

main()
