# Administrator accounts list
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]

# Build your login functions below
def getCreds():
        username = input("What is your username? ")
        password = input("What is your password? ")




        return {"username": username, "password": password}


def checkLogin(adminList, user_info):
    if user_info in adminList:
        logged_In = True
        print("CONGRATS YOU'RE IN")
    else: 
        logged_In = False
        print("------")
        print("YOU SUCK TRY AGAIN")
        print("------")
        retry = getCreds()
        return 


while True:
    user_info = getCreds()
    is_admin = checkLogin(adminList, user_info)
    print("-----")
    if is_admin:
        print("CONGRATS YOU'RE IN!")
        break
    else:
        ("YOU SUCK TRY AGAIN")