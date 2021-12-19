#!/usr/bin/env python3
# Logon v2 scvript
import os, sys, time, hashlib, platform
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image

class Login(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = "Login")
        self.resizable(0,0)
        #self.style = Style()
        #self.style.theme_use("clam")
        self.ttkStyle = ThemedStyle()
        self.ttkStyle.set_theme("arc")
        self.configure(background = 'white')
        if platform.system() == 'Darwin':
            icon = ImageTk.PhotoImage(Image.open('icon.png'))
        else:
            icon = PhotoImage(file='icon.png')
        #icon = PhotoImage(file='icon.png') # This only works on Linux and Windows
        self.tk.call('wm', 'iconphoto', self._w, icon)
        if platform.system() == 'Linux' or platform.system() == 'Darwin':
            self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        else:
            pass

        self.bind("<Escape>", self.exit) # Press ESC to quit app

        self.options = {
            'username' : StringVar(),
            'pwd' : StringVar(),
            'reg_username' : StringVar(),
            'reg_password' : StringVar(),
            'reg_check_password' : StringVar(),
        }

        if platform.system() == 'Darwin':
            photo = ImageTk.PhotoImage(Image.open('images/login_img.png'))
        else:
            photo = PhotoImage(file='images/login_img.png')

        #photo = PhotoImage(file='images/login_img.png') # This only works on Linux and Windows
        #photo = photo.zoom(2)
        #photo = photo.subsample(1)
        label = Label(self, image=photo, background = 'white')
        label.image = photo # keep a reference!
        label.grid(row = 0, column = 0, columnspan = 2)

        Label(self, text = 'Username', background = 'white', foreground = 'black', font='Helvetica 12 bold').grid(row = 1, column = 0, sticky = 'w')
        self.a = Entry(self, textvariable = self.options['username'], width = 31)
        self.a.grid(row = 2, column = 0, columnspan = 2, sticky = 'w')
        self.a.focus()

        Label(self, text = 'Password', background = 'white', foreground = 'black', font='Helvetica 12 bold').grid(row = 3, column = 0, sticky = 'w')
        Entry(self, textvariable = self.options['pwd'], show = '*', width = 31).grid(row = 4, column = 0, columnspan = 2, sticky = 'w')

        login_clk = Button(self, text = 'Login', command = self.login, width = 30).grid(row = 5, column = 0, columnspan = 2, sticky = 'w')
        register_clk = Button(self, text = 'Register', command = self.register, width = 30).grid(row = 6, column = 0, columnspan = 2, sticky = 'w')
        close = Button(self, text = 'Exit', command = self.destroy, width = 30).grid(row = 7, column = 0, columnspan = 2, sticky = 'w')
        self.bind("<Return>", self.login_event) # Press ESC to quit app

    def login_event(self, event):
        self.login() # Redirect to login on event (hotkey is bound to <Return>)

    def login(self):
        # Check username and password
        check_pwd = hashlib.sha256(self.options['pwd'].get().encode('utf-8')).hexdigest()

        for user in open('./users.txt').readlines():
            if self.options['username'].get() == user.split(':')[0].strip() and check_pwd == user.split(':')[1].strip():
                self.destroy()
                main = MainWindow(self.options['username'].get(), self.options['pwd'].get())
                main.mainloop()
            #else:
            #    print(user.split(':')[0])

        messagebox.showwarning('ERROR', 'Invalid username or password!')

    def exit(self, event):
        sys.exit(0)

    def register(self):
        self.reg = Toplevel()
        self.reg.title(string = 'Register')
        self.reg.configure(background = 'white')
        self.reg.resizable(0,0)

        if platform.system() == 'Darwin':
            reg_photo = ImageTk.PhotoImage(Image.open('images/register.png'))
        else:
            reg_photo = PhotoImage(file='images/register.png')
        #reg_photo = PhotoImage(file='images/register.png')
        #photo = photo.zoom(2)
        #reg_photo = reg_photo.subsample(2)
        label = Label(self.reg, image=reg_photo, background = 'white')
        label.image = reg_photo # keep a reference!
        label.grid(row = 0, column = 0, columnspan = 2)

        check = '' # Confirm password variable

        Label(self.reg, text = 'Username', background = 'white').grid(row = 1, column = 0)
        self.options['reg_username'] = Entry(self.reg, textvariable = self.options['reg_username'], width = 30)
        self.options['reg_username'].grid(row = 2, column = 0, columnspan = 2)
        self.options['reg_username'].focus()

        Label(self.reg, text = 'Password', background = 'white').grid(row = 3, column = 0)
        self.options['reg_password'] = Entry(self.reg, textvariable = self.options['reg_password'], width = 30, show = '*')
        self.options['reg_password'].grid(row = 4, column = 0, columnspan = 2)

        Label(self.reg, text = 'Confirm Password', background = 'white').grid(row = 5, column = 0)
        self.options['reg_check_password'] = Entry(self.reg, textvariable = self.options['reg_check_password'], width = 30, show = '*')
        self.options['reg_check_password'].grid(row = 6, column = 0, columnspan = 2)

        register_button = Button(self.reg, text = 'Register', command = self.register_user, width = 30)
        register_button.grid(row = 7, column = 0, columnspan = 2)
        self.reg.bind('<Return>', self.register_user_event)
        close_register = Button(self.reg, text = 'Cancel', command = self.reg.destroy, width = 30).grid(row = 8, column = 0, columnspan = 2)


    def register_user_event(self, event):
        self.register_user()

    def register_user(self):

        # Check if passwords match
        if not self.options['reg_password'].get() == self.options['reg_check_password'].get():
            messagebox.showwarning('ERROR', 'Passwords do not match!')
            return
        else:
            pass

        # Check if every entry was filled
        if self.options['reg_username'].get() == '' or self.options['reg_password'].get() == '':
            messagebox.showwarning("ERROR", "Not all fields were filled!")
            return
        else:
            pass

        # check if username already exists
        try:
            for user in open('./users.txt').readlines():
                if user.split(':')[0] == self.options['reg_username'].get():
                    messagebox.showwarning('ERROR', 'Username already exists!')
                    return
                else:
                    pass
        except Exception:
            pass

        # Write data to local file
        with open('./users.txt', 'a+') as f:
            f.write('%s:%s\n' % (self.options['reg_username'].get(), hashlib.sha256(self.options['reg_password'].get().encode('utf-8')).hexdigest()))
            f.close()

        messagebox.showinfo('INFO', 'User registered!')

        self.reg.destroy()

class MainWindow(Tk):
    def __init__(self, username, pwd):
        Tk.__init__(self)
        self.title(string = "Welcome, %s" % username)
        self.resizable(0,0)
        #self.style = Style()
        #self.style.theme_use("clam")
        self.ttkStyle = ThemedStyle()
        self.ttkStyle.set_theme("arc")
        self.configure(background = 'white')
        if platform.system() == 'Darwin':
            icon = ImageTk.PhotoImage(Image.open('icon.png'))
        else:
            icon = PhotoImage(file='icon.png')
        #icon = PhotoImage(file='icon.png')
        self.tk.call('wm', 'iconphoto', self._w, icon)
        self.protocol("WM_DELETE_WINDOW", self.on_close_event)
        if platform.system() == 'Linux' or platform.system() == 'Darwin':
            self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        else:
            pass

        self.bind("<Escape>", self.exit) # Press ESC to quit app


        self.options = {
            'username' : StringVar(),
            'pwd' : StringVar(),
        }

        if platform.system() == 'Darwin':
            photo = ImageTk.PhotoImage(Image.open('images/login_img.png'))
        else:
            photo = PhotoImage(file='images/login_img.png')
        #photo = PhotoImage(file='images/login_img.png')
        #photo = photo.zoom(2)
        #photo = photo.subsample(1)
        label = Label(self, image=photo, background = 'white')
        label.image = photo # keep a reference!
        label.grid(row = 0, column = 0, columnspan = 2)

    def exit(self, event):
        self.on_close_event()

    def on_close_event(self):
        result = messagebox.askyesno("Are you sure?","Are you sure you want to exit?")
        if result == False:
            return
        else:
            pass

        sys.exit(0)

logon = Login()
logon.mainloop()
