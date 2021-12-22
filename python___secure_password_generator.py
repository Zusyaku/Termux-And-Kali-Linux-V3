#-------------------------------------------------------------------------------
# Name:        Password Generator
# Purpose:
#
# Author:      Kansas
#
# Created:     14/12/2013
# Copyright:   (c) Kansas 2013
# Licence:     None
#-------------------------------------------------------------------------------
import random
import hashlib
from Tkinter import *
import tkMessageBox

def resetBox():
    length.delete(0, END)

def genPassword():
    end = int(length.get())
    i = 1
    password = ''
    while(i <= end):
        choice = int(float(random.uniform(1,12)))
        if choice <= 3:
            #reg char
            password = password + random.choice('abcdefghijklmnopqrstuvwxyz')
            i+=1
        else:
            if choice <= 6:
                #capitalized char
                password = password + random.choice('abcdefghijklmnopqrstuvwxyz').upper()
                i+=1
            else:
                if choice <= 9:
                    #sym
                    password = password + random.choice('~`!@#$%^&*()_-+={}[]|\\:;"\'<,>.?/')
                    i+=1
                else:
                    if choice <= 12:
                        #int
                        password = password + random.choice('0123456789')
                        i+=1
                    else:
                        print ''
    root.clipboard_clear()
    root.clipboard_append(password)
    tkMessageBox.showinfo("Password", "The generated password %s was copied to your clipboard." % password)

if __name__ == '__main__':
    root = Tk()
    root.title("Secure Password Generator")
    root.geometry("350x130")
    root.resizable(0,0)

    title = Label(root, text="Secure Password Generator", font=("Arial", 18))
    title.pack()

    frame = Frame(root, relief=SUNKEN, height=2, bd=1)
    frame.pack(fill=X, padx=5)

    framemid = Frame(root, relief=FLAT, borderwidth=1)
    framemid.pack(fill=X, expand=1)

    instructions = Label(framemid, text="Password Length: ")
    instructions.pack(side='left', padx=15)

    length = Entry(framemid, width=30)
    length.pack(side='left')

    framebottom = Frame(root, relief=SUNKEN, height=2, bd=1)
    framebottom.pack(fill=X, padx=5)

    reset = Button(root, text="Reset", width=10, padx=1, pady=1, command=resetBox)
    reset.pack(side='right', padx=5)
    generator = Button(root, text="Generate", width=10, padx=1, pady=1, command=genPassword)
    generator.pack(side='right', anchor='s', padx=5, pady=5)

    root.mainloop()