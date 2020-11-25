
import sys

login_pass = "password"
pass_list = {
    "youtube": "123456",
    "gmail": "09876",
    "skype": "cat-dog"
}
# check login credentials
def login():
    while True:
        usr_inp_1 = input("What is the password?\n")
        if usr_inp_1 == "q":
            sys.exit(0)
        elif usr_inp_1 == login_pass:
            print("Welcome!\n")
            manager()
        else:
            print("Incorrect password\n")
            continue
# get passwords from manager
def manager():
    while True:
        usr_inp_2 = input("Which password do you want?\n")
        if usr_inp_2 == "q":
            sys.exit(0)
        elif usr_inp_2 in pass_list:
            print(pass_list.get(usr_inp_2) + "\n")
            continue
        else:
            print("not a valid selection\n")
            continue
login()