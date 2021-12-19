#!/usr/bin/python
import os, sys, random, string, hashlib, subprocess, signal, socket, select, threading, time, base64, time
from Tkinter import *
from ttk import *

try:
    from Crypto import Random
    from Crypto.Cipher import AES
except ImportError:
    print('Python Crypto is not installed, please do: apt install python-crypto -y\nThen try again'); sys.exit(1)

BS = 256
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

class AESCipher:
    def __init__(self, key ):
        self.key = key

    def encrypt(self, raw ):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt( enc[16:]))

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title(string = " << SPyChat | Secure version >> ")
        self.resizable(0,0)
        self.style = Style()
        self.style.theme_use("clam")

        self.options = {
            'host' : StringVar(),
            'port' : IntVar(),
            'username' : StringVar(),
            'key' : StringVar(),
            'chatbar' : StringVar(),
        }

        self.options['host'].set('0.0.0.0')
        self.options['port'].set(8989)

        settings = LabelFrame(self, text = 'Server', relief = GROOVE, labelanchor = 'nw', width = 570, height = 110)
        settings.grid(row = 0, column = 1)
        settings.grid_propagate(0)

        # Host entry
        Label(settings, text = 'Host:').grid(row = 0, column = 1)
        Entry(settings, textvariable = self.options['host']).grid(row = 0, column = 2, columnspan = 2)

        # Port entry
        Label(settings, text = 'Port:').grid(row = 1, column = 1)
        Entry(settings, textvariable = self.options['port']).grid(row = 1, column = 2, columnspan = 2)

        # Username entry
        Label(settings, text = 'Username:').grid(row = 2, column = 1)
        username_entry = Entry(settings, textvariable = self.options['username']).grid(row = 2, column = 2, columnspan = 2)

        # Key entry
        Label(settings, text = 'Key:').grid(row = 3, column = 1)
        key_entry = Entry(settings, textvariable = self.options['key'], show = '*').grid(row = 3, column = 2, columnspan = 2)

        # Chat Frame
        chat = LabelFrame(self, text = 'Chat', relief = GROOVE)
        chat.grid(row = 3, column = 1, rowspan = 4)
        self.options['chatbox'] = Text(chat, foreground="white", background="black", highlightcolor="white", highlightbackground="black", height = 28, width = 80)
        self.options['chatbox'].grid(row = 0, column = 1)

        # Tags
        self.options['chatbox'].tag_configure('yellow', foreground='yellow')
        self.options['chatbox'].tag_configure('red', foreground='red')
        self.options['chatbox'].tag_configure('deeppink', foreground='deeppink')
        self.options['chatbox'].tag_configure('red', foreground='red')
        self.options['chatbox'].tag_configure('orange', foreground='orange')
        self.options['chatbox'].tag_configure('bold', font='bold')

        self.options['chatbox'].insert('1.0', 'Set Host and port, then click Connect to enter a server.\nOr click Host to host a chat server on the given port\n', 'bold')

        # Connect button
        connect_button = Button(self, text = "Connect!", command = self.connect, width = 68).grid(row = 1, column = 0, columnspan = 2)

        # Host button
        host_server_button = Button(self, text = "Host", command = self.host, width = 68).grid(row = 2, column = 0, columnspan = 2)

        # Send text entry
        self.options['chatbar'] = Entry(chat, textvariable = self.options['chatbar'], width = 70)
        self.options['chatbar'].grid(row = 1, column = 0, columnspan = 4)
        submit = Button(self, text = "Submit", command = self.send_message, width = 68).grid(row = 7, column = 0, columnspan = 2)
        self.options['chatbar'].bind('<Return>', self.send_message) # Send message with the Return key (aka Enter)
        self.options['chatbar'].focus()

    # Socket connection
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    def connect(self):
        self.options['chatbox'].insert('1.0', 'Attempting to connect as %s to %s:%s....\n' % (self.options['username'].get(), self.options['host'].get(), self.options['port'].get()), 'yellow')
        global cipher
        cipher = AESCipher(self.options['key'].get()) # Set cipher

        # Start thread
        thread = threading.Thread(target=self.keep_alive)
        thread.daemon = True
        thread.start()

    def exit(self):
        sys.exit(0)

    def keep_alive(self):
        try:
            s.connect((self.options['host'].get(), int(self.options['port'].get())))
            #self.options['chatbox'].insert('1.0', 'Connected, Welcome!\n', 'bold')
            connect_button = Button(self, text = "Quit", command = self.exit, width = 70).grid(row = 1, column = 0, columnspan = 2)
            s.send(cipher.encrypt('USER$' + self.options['username'].get()))
        except Exception as e:
            self.options['chatbox'].insert('1.0', 'Failed to connect: %s\n' % e, 'red')

        running = True

        while running:
            socket_list = [sys.stdin, s]

            # Get the list sockets which are readable
            read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])

            for sock in read_sockets:
                if sock == s:
                    data = sock.recv(1024)
                    try:
                        data = cipher.decrypt(data)
                    except Exception:
                        pass

                    if not data:
                        self.options['chatbox'].insert('1.0', 'Disconnected from server\n', 'red')
                        sys.exit(1)
                    else:
                        # Show data
                        if data.startswith('[SERVER]'):
                            self.options['chatbox'].insert('1.0', '[%s] %s\n' % (time.strftime('%X'),data.strip()), 'deeppink')

                        else:
                            self.options['chatbox'].insert('1.0', '[%s] %s\n' % (time.strftime('%X'),data.strip()), 'yellow')

    def send_message(self, event):
        # Send message
        message = '[%s] %s ' % (self.options['username'].get(), self.options['chatbar'].get())
        self.options['chatbox'].insert('1.0', '[%s] %s\n' % (time.strftime('%X'), message)) # Insert on top
        s.send(cipher.encrypt(message)) # Send message
        self.options['chatbar'].delete(0, END) # Clear chatbar

    def host(self):
        key = hashlib.md5(gen_string()).hexdigest()
        self.options['chatbox'].insert('1.0', '\nYour key: %s\n' % key, 'yellow')
        self.options['chatbox'].insert('1.0', 'Others need this key to connect with your server to secure the connection\n')

        # Open server
        server = subprocess.Popen(['python ./server.py %s %i %s' % (self.options['host'].get(), int(self.options['port'].get()), key)], stdout=subprocess.PIPE, shell=True)

        # Change to stop server button
        host_server_button = Button(self, text = "Stop server", command = self.stop_server, width = 70).grid(row = 2, column = 0, columnspan = 2)


    def stop_server(self):
        try:
            proc = subprocess.Popen("netstat -tulpn | grep %s" % self.options['port'].get(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            pid, err = proc.communicate()

            pid = pid.split('/')
            pid[0] = pid[0].split(' ')
            print(pid[0][-1])

            # Kill PID
            os.kill(int(pid[0][-1]), signal.SIGKILL)

            # Change button to host
            host_server_button = Button(self, text = "Host", command = self.host, width = 70).grid(row = 2, column = 0, columnspan = 2)

        except Exception as e:
            print(e)
            pass

        self.options['chatbox'].insert('1.0', 'Server closed... Killed PID %i\n' % int(pid[0][-1]))

# Generate a key for server hosting
def gen_string(size=32, chars=string.ascii_uppercase + string.digits):
      return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    try:
        main = MainWindow()
        main.mainloop()
    except Exception as e:
        print('There was an error: %s\n' % e)
