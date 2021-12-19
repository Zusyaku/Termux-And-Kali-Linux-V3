#!/usr/bin/python
import socket, select, os, sys, time, base64
from Crypto import Random
from Crypto.Cipher import AES

if len(sys.argv) < 4:
    print('Usage: python server.py <host> <port> <key>')
    sys.exit(1)

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

host = sys.argv[1]
port = sys.argv[2]
cipher = AESCipher(sys.argv[3])

SOCKET_LIST = [] # List with connected sockets

def server(host, port):
    running = True

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, int(port)))
    server_socket.listen(10)

    SOCKET_LIST.append(server_socket)

    #print("Chat server started on port %i" % int(port))

    while running:
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)

        for sock in ready_to_read:
            # a new connection request recieved
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)

                # Sent welcome to just that client.
                sockfd.send(cipher.encrypt('[SERVER] Welcome, you connected from %s:%s' % addr))
            else:
                try:
                    data = sock.recv(1024)
                    try:
                        data = cipher.decrypt(data)
                    except Exception:
                        pass

                    if '$' in data:
                        if data.split('$')[0] == 'USER':
                            username = data.split('$')[1]
                            message = '[SERVER] %s entered the server with id %s' % (username, addr[1])
                            broadcast(server_socket, sockfd, cipher.encrypt(message))

                    elif data:
                        data = data.strip()
                        # Send data to all clients
                        message = '\r[%s] %s' % (addr[1], data)
                        broadcast(server_socket, sock, cipher.encrypt(message))

                    else:
                        # remove the socket that's broken
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        broadcast(server_socket, sock, cipher.encrypt("Client [%s] left\n") % addr[1])

                except:
                    broadcast(server_socket, sock, cipher.encrypt("Client left\n"))
                    continue

    server_socket.close()

# broadcast chat messages to all connected clients
def broadcast(server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try:
                socket.send(message)
            except:
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)

# Start server
server(host, int(port))
