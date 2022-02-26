import tkinter
from tkinter import *
import random
from tkinter import messagebox

# you can add more words as per your requirement
Answers = [
   "3",
   "8",
   "2",
   "0",
   "0",
   "0",
   "1",
]

Numbers = [
   "5+1_=18",
   "6+1_+13=37",
   "5+1_+2=19",
   "1_+6+13=29",
   "8+15+1_=30",
   "2_+17=37",
   "1_+19=30"   ,
]

# I have improvised the code by using len(words)
num =  random.randrange(0, len(Numbers), 1)

def default():
    global Numbers,Answers,num
    lbl.config(text = Numbers[num])

def res():
    global Numbers,Answers,num
    num = random.randrange(0, len(Numbers), 1)
    lbl.config(text = Numbers[num])
    point.delete(0, END)


def checkAnswer():
    global Numbers, Answers,num
    var = point.get()
    if var == Answers[num]:
        messagebox.showinfo("Success", "Answer is Correct")
        res()
    else:
        messagebox.showerror("Error", "incorrect")
        point.delete(0, END)




root = tkinter.Tk()
root.geometry("550x400+400+500")
root.title("Guess Numbers")
root.configure(background = "#2C3335")

lbl = Label(
    root,
    text = "Start",
    font = ("Roboto", 18),
    bg = "#4C4B4B",
    fg = "White",
)
lbl.pack(pady = 30,ipady=10,ipadx=10)


ans1 = StringVar()
point = Entry(
    root,
    font = ("Roboto", 16),
    textvariable = ans1,
)
point.pack(ipady=5,ipadx=5)

btncheck = Button(
    root,
    text = "Check",
    font = ("Roboto Bold", 16),
    width = 16,
    bg = "#2F363F",
    fg = "White",
    relief = GROOVE,
    command = checkAnswer,
)
btncheck.pack(pady = 40)

btnreset = Button(
    root,
    text = "Reset",
    font = ("Roboto", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#EA425C",
    relief = GROOVE,
    command = res,
)
btnreset.pack()

default()
root.mainloop()
