
from tkinter import *
from db import User

def Submit():
    name = namee.get()
    email = emaile.get()
    password = passe.get()
    User(name,email,password)

root = Tk()
root.geometry('400x400')

lable = Label(text = 'SignUp').pack()

namel = Label(text = 'Name').pack()
namee = Entry()
namee.pack()

emaill = Label(text = 'Email').pack()
emaile = Entry()
emaile.pack()

passl = Label(text = 'Password').pack()
passe = Entry()
passe.pack()

sumbit = Button(text= 'Submit',command= Submit).pack()

root.mainloop() 