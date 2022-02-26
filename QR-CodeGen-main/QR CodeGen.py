import tkinter as tk
import qrcode
import tkinter as tk
from tkinter import *
import os

def QR():
 qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=5

	)

 text = entry.get() 
 qr.add_data(text)
 qr.make(fit=True)
 img=qr.make_image(fill="black",back_color="white")
 img.save("1.png")

#Window
window = tk.Tk()
window.title("Type Your OR Link")
window.geometry("300x150")
window.configure(background = "#2C3335")
#InputSpace
entry = StringVar()
point = Entry(
    window,
    font = ("Roboto", 16),
    textvariable = entry,
)
point.grid(pady=20, padx=25, ipady=5, ipadx=5)


#Button
button = tk.Button(window, text="OK", command=QR)
button.grid(ipady=5,ipadx=25)
            
            
window.mainloop()