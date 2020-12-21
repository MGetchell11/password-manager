from tkinter import *
import string
import secrets

# Display randomly generated password
def password_gen():
    alphabet = string.ascii_letters + string.digits + '-_!*'
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        if (any(c.islower() for c in password) >= 4
                and sum(c.isupper() for c in password) >= 4
                and sum(c.isdigit() for c in password) >= 4):
            break
        Label(text=password, font="Calibri").pack()
        break

# Display passwords
def password_list():
    Label(text="gmail = 123456\nyahoo = 98765\nspotify = password123\nsteam = 13579", font="Calibri").pack()

# Start Screen with buttons to redirect
def main_screen():
    first_screen = Tk()
    first_screen.geometry("300x250")
    first_screen.title("Password Manager")
    Button(text="Get Passwords", height="2", width="30", command=password_list).pack()
    Button(text="Generate Random Password", height="2", width="30", command=password_gen).pack()
    first_screen.mainloop()
main_screen()
