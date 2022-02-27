require "socket"

sock = TCPServer.new(1337)

loop do
  client = sock.accept()

  puts("client conneted")
  while 1
    print("Command#")
    command = gets.chomp
    client.puts(command)
    puts("#{command}")
end
end
