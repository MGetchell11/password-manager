from tkinter import *

def screen_2():
    second_screen = Tk()
    second_screen.geometry("300x250")
    second_screen.title("Passwords Updated!")
    Label(text="gmail = 123456\nyahoo = 98765\nspotify = password123\nsteam = 13579", font="Calibri").pack()
def screen_1():
    first_screen = Tk()
    first_screen.geometry("300x250")
    first_screen.title("Password Manager")
    Button(text="Get Passwords", height="2", width="30", command=screen_2).pack()
    first_screen.mainloop()
screen_1()
