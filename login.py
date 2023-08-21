from tkinter import Button, Entry, Label, Tk
from db import login

def Submit():
    name = namee.get()
    password = passe.get()
    login(name,password)

root = Tk()
root.geometry('400x400')

lable = Label(text = 'LOGIN').pack()

namel = Label(text = 'Name').pack()
namee = Entry()
namee.pack()

passl = Label(text = 'Password').pack()
passe = Entry()
passe.pack()

sumbit = Button(text= 'Submit',command= Submit).pack()

root.mainloop() 