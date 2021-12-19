#!/usr/bin/env python3
'''
PyChat v3

Compile with:
pyinstaller -F -w -i icon.ico --hidden-import tkinter --hidden-import tkinter.ttk --hidden-import ttkthemes --hidden-import pycrypto --add-data 'images/*:images' --add-data 'users.txt:.' PyChat.py
'''
import os, sys, random, string, hashlib, subprocess, socket, select, threading, time, base64, platform
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ttkthemes import ThemedStyle
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from PIL import ImageTk, Image

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def encrypt(key, source, encode=True):
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = Random.new().read(AES.block_size)  # generate IV
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    return base64.b64encode(data).decode("latin-1") if encode else data

def decrypt(key, source, decode=True):
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = source[:AES.block_size]  # extract the IV from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])  # decrypt
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding

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
        icon = ImageTk.PhotoImage(Image.open(resource_path('images/icon.png')))
        self.tk.call('wm', 'iconphoto', self._w, icon)
        if platform.system() == 'Linux':
            self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        else:
            pass

        self.bind("<Escape>", self.exit) # Press ESC to quit app

        self.options = {
            'username' : StringVar(),
            'host' : StringVar(),
            'port' : IntVar(),
            'key' : StringVar(),
            'pwd' : StringVar(),
            'reg_username' : StringVar(),
            'reg_password' : StringVar(),
            'reg_check_password' : StringVar(),
        }

        # Set default values
        self.options['host'].set('0.0.0.0')
        self.options['port'].set(8989)

        if platform.system() == 'Darwin':
            photo = ImageTk.PhotoImage(Image.open(resource_path('images/login_img.png')))
        else:
            photo = PhotoImage(file='images/login_img.png')
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
        Entry(self, textvariable = self.options['pwd'], width = 31, show = '*').grid(row = 4, column = 0, columnspan = 2, sticky = 'w')

        Label(self, text = 'Server Password', background = 'white', foreground = 'black', font='Helvetica 12 bold').grid(row = 5, column = 0, sticky = 'w')
        Entry(self, textvariable = self.options['key'], width = 31, show = '*').grid(row = 6, column = 0, columnspan = 2, sticky = 'w')

        Label(self, text = 'Host', background = 'white', foreground = 'black', font='Helvetica 12 bold').grid(row = 7, column = 0, sticky = 'w')
        Entry(self, textvariable = self.options['host'], width = 31).grid(row = 8, column = 0, columnspan = 2, sticky = 'w')

        Label(self, text = 'Port', background = 'white', foreground = 'black', font='Helvetica 12 bold').grid(row = 9, column = 0, sticky = 'w')
        Entry(self, textvariable = self.options['port'], width = 31).grid(row = 10, column = 0, columnspan = 2, sticky = 'w')

        login_clk = Button(self, text = 'Login', command = self.login, width = 30).grid(row = 11, column = 0, columnspan = 2, sticky = 'w')
        register_clk = Button(self, text = 'Register', command = self.register, width = 30).grid(row = 12, column = 0, columnspan = 2, sticky = 'w')
        close = Button(self, text = 'Exit', command = self.destroy, width = 30).grid(row =13, column = 0, columnspan = 2, sticky = 'w')
        self.bind("<Return>", self.login_event) # Press ESC to quit app

    def login_event(self, event):
        self.login() # Redirect to login on event (hotkey is bound to <Return>)

    def login(self):
        # Check username and password
        check_pwd = hashlib.sha256(self.options['pwd'].get().encode('utf-8')).hexdigest()

        for user in open(resource_path('./users.txt')).readlines():
            if self.options['username'].get() == user.split(':')[0].strip() and check_pwd == user.split(':')[1].strip():
                self.destroy()
                main = MainWindow(self.options['username'].get(), self.options['host'].get(), self.options['port'].get(), self.options['key'].get())
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

        reg_photo = Image.open(resource_path('images/login_img.png'))
        #photo = photo.zoom(2)
        reg_photo = reg_photo.resize((150,150), Image.ANTIALIAS)
        reg_photo = ImageTk.PhotoImage(reg_photo)

        label = Label(self.reg, image=reg_photo, background = 'white')
        label.image = reg_photo # keep a reference!
        label.grid(row = 0, column = 0, columnspan = 2)

        check = '' # Confirm password variable

        Label(self.reg, text = 'Username', background = 'white').grid(row = 1, column = 0, sticky = 'w')
        self.options['reg_username'] = Entry(self.reg, textvariable = self.options['reg_username'], width = 30)
        self.options['reg_username'].grid(row = 2, column = 0, columnspan = 2)
        self.options['reg_username'].focus()

        Label(self.reg, text = 'Password', background = 'white').grid(row = 3, column = 0, sticky = 'w')
        self.options['reg_password'] = Entry(self.reg, textvariable = self.options['reg_password'], width = 30, show = '*')
        self.options['reg_password'].grid(row = 4, column = 0, columnspan = 2)

        Label(self.reg, text = 'Confirm Password', background = 'white').grid(row = 5, column = 0, sticky = 'w')
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
            for user in open(resource_path('./users.txt')).readlines():
                if user.split(':')[0] == self.options['reg_username'].get():
                    messagebox.showwarning('ERROR', 'Username already exists!')
                    return
                else:
                    pass
        except Exception:
            pass

        # Write data to local file
        with open(resource_path('./users.txt'), 'a+') as f:
            f.write('%s:%s\n' % (self.options['reg_username'].get(), hashlib.sha256(self.options['reg_password'].get().encode('utf-8')).hexdigest()))
            f.close()

        messagebox.showinfo('INFO', 'User registered!')

        self.reg.destroy()

class MainWindow(Tk):
    def __init__(self, username, host, port, server_pwd):
        Tk.__init__(self)
        self.title(string = "PyChat | Welcome, %s" % username)
        self.resizable(0,0)
        #self.style = Style()
        #self.style.theme_use("clam")
        self.ttkStyle = ThemedStyle()
        self.ttkStyle.set_theme("arc")
        self.configure(background = 'white')
        icon = ImageTk.PhotoImage(Image.open(resource_path('images/icon.png')))
        self.tk.call('wm', 'iconphoto', self._w, icon)
        self.protocol("WM_DELETE_WINDOW", self.on_close_event)
        if platform.system() == 'Linux':
            self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        else:
            pass

        global user
        global key
        global h
        global p
        user = username
        key = server_pwd
        key = key.encode('utf-8') # encode to type bytes
        h = host
        p = port

        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)

        self.bind("<Escape>", self.exit) # Press ESC to quit app

        self.options = {
            'chatbar' : StringVar(),
        }

        self.options['chatbox'] = Text(self, foreground="black", background="white", highlightcolor="white", highlightbackground="black", height = 28, width = 80)
        self.options['chatbox'].grid(row = 0, column = 0)

        # Tags
        self.options['chatbox'].tag_configure('yellow', foreground='yellow')
        self.options['chatbox'].tag_configure('red', foreground='red')
        self.options['chatbox'].tag_configure('deeppink', foreground='deeppink')
        self.options['chatbox'].tag_configure('orange', foreground='orange')
        self.options['chatbox'].tag_configure('bold', font='bold')

        self.options['chatbox'].insert(END, '[SYSTEM] Do /help to view a list with commands.\n', 'deeppink')

        '''
        User list is on my ToDo list.
        self.options['users'] = Listbox(self, width = 30, height = 30)
        self.options['users'].grid(row = 0, column = 1, rowspan = 3, sticky = 'n')
        self.options['users'].insert(END, 'Online Users:')
        '''
        # Send text entry
        self.options['chatbar'] = Entry(self, textvariable = self.options['chatbar'], width = 79)
        self.options['chatbar'].grid(row = 1, column = 0, columnspan = 4, sticky = 'w')
        self.options['chatbar'].bind('<Return>', self.send_message_event) # Send message with the Return key (aka Enter)
        self.options['chatbar'].focus()

        submit = Button(self, text = "Submit", command = self.send_message, width = 78).grid(row = 2, column = 0, columnspan = 2, sticky = 'w')

        try:
            self.connect()
        except Exception as e:
            self.options['chatbox'].insert(END, '[ERROR] %s\n' % e, 'red')


    def send_message_event(self, event):
        self.send_message()

    def connect(self):
        self.options['chatbox'].insert(END, '[SYSTEM] Attempting to connect to %s:%i as %s\n' % (h, int(p), user), 'deeppink')

        # Start thread
        thread = threading.Thread(target=self.keep_alive)
        thread.daemon = True
        thread.start()

    def keep_alive(self):
        online = []
        try:
            s.connect((h, int(p)))
            self.options['chatbox'].insert(END, '[SYSTEM] Connected!\n', 'deeppink')
            self.options['chatbox'].see(END)
            #foo = 'USER$' + user
            #s.send(foo.encode('utf-8'))

            message = 'USER$' + user
            message = message.encode('utf-8')
            message = encrypt(key, message)
            s.send(message.encode('utf-8')) # Send message
        except Exception as e:
            self.options['chatbox'].insert(END, '[ERROR] %s\n' % e, 'red')
            self.options['chatbox'].see(END)
            messagebox.showwarning('ERROR', '%s' % e)
            return

        while True:
            socket_list = [sys.stdin, s]

            # Get the list sockets which are readable
            read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

            for sock in read_sockets:
                if sock == s:
                    data = sock.recv(1024)

                    try:
                        data = decrypt(key, data.decode('utf-8'))
                    except Exception as e:
                        print(e)
                        pass

                    data = data.decode('utf-8')
                    #print(data)

                    if not data:
                        self.options['chatbox'].insert(END, 'Disconnected from server\n', 'red')
                        self.options['chatbox'].see(END)
                        return False
                    else:
                        # Show data
                        if data.startswith('[SERVER]'):
                            self.options['chatbox'].insert(END, '[%s] %s\n' % (time.strftime('%X'),data.strip()), 'deeppink')
                            self.options['chatbox'].see(END)
                        elif data.startswith('POKE$'):
                            if user == data.split('$')[1]:
                                message = 'ONLINE$%s$%s' % (data.split('$')[1], data.split('$')[2])
                                message = message.encode('utf-8')
                                message = encrypt(key, message)
                                s.send(message.encode('utf-8')) # Send message
                                messagebox.showinfo('Pssst, hey!', '%s poked you!' % data.split('$')[2])
                        elif data.startswith('ONLINE$'):
                            if user == data.split('$')[2]:
                                messagebox.showinfo('True', '%s is online!' % data.split('$')[1])
                        else:
                            self.options['chatbox'].insert(END, '[%s] %s\n' % (time.strftime('%X'),data.strip()), 'orange')
                            self.options['chatbox'].see(END)


    def send_message(self):
        if self.options['chatbar'].get() != '':
            pass
        else:
            return

        if self.options['chatbar'].get() == '/clear' or self.options['chatbar'].get() == '/cls':
            self.options['chatbar'].delete(0, END) # Clear chatbar
            self.options['chatbox'].delete('1.0', END) # Clear chatbox
        elif self.options['chatbar'].get() == '/whoami':
            self.options['chatbar'].delete(0, END) # Clear chatbar
            messagebox.showinfo('INFO', 'You are: %s' % user)
        elif self.options['chatbar'].get() == '/quit' or self.options['chatbar'].get() == '/exit':
            sys.exit(0)
        elif self.options['chatbar'].get() == '/help':
            message = '''Listing commands for non-root users...
Commands:
        /help       | View this help
        /whoami     | Show as which username you're connected
        /poke       | Poke a user and see if they're online or not
        /clear      | Clear chatbox
        /cls        | Alias for /clear
        /quit       | Shutdown application
        /exit       | Alias for /quit
            '''
            self.options['chatbox'].insert(END, '[SYSTEM] %s\n' % (message), 'deeppink')
            self.options['chatbar'].delete(0, END) # Clear chatbar
            self.options['chatbox'].see(END)
        elif self.options['chatbar'].get().startswith('/poke'):
            message = 'POKE$%s$%s' % (self.options['chatbar'].get().split(' ')[1], user)
            self.options['chatbox'].insert(END, '[%s] [SYSTEM] You poked %s\n' % (time.strftime('%X'), self.options['chatbar'].get().split(' ')[1]), 'deeppink')
            message = message.encode('utf-8')
            message = encrypt(key, message)
            s.send(message.encode('utf-8')) # Send message
            self.options['chatbar'].delete(0, END) # Clear chatbar
            self.options['chatbox'].see(END)
        else:
            message = '[%s] %s ' % (user, self.options['chatbar'].get())
            self.options['chatbox'].insert(END, '[%s] %s\n' % (time.strftime('%X'), message))
            message = message.encode('utf-8')
            message = encrypt(key, message)
            s.send(message.encode('utf-8')) # Send message
            self.options['chatbar'].delete(0, END) # Clear chatbar
            self.options['chatbox'].see(END)

    def exit(self, event):
        self.on_close_event()

    def on_close_event(self):
        result = messagebox.askyesno("Are you sure?","Are you sure you want to exit?")
        if result == False:
            return
        else:
            pass

        try:
            message = 'LEFT$%s' % user
            message = message.encode('utf-8')
            message = encrypt(key, message)
            s.send(message.encode('utf-8')) # Send message
        except Exception: # If not connected with a server, pass and close
            pass

        sys.exit(0)

logon = Login()
logon.mainloop()
