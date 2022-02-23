import socket

# socket instantiation. create socket object
my_socket = socket.socket(socket.AF_INET,
                          socket.SOCK_STREAM)
# connect existing socket to destination. Server DNS: data.pr4e.org, port 80
my_socket.connect(('data.pr4e.org', 80))
# send GET request
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_socket.send(cmd)

# receive data and "read" it periodically in chunks of 512 characters
# until there is no more data (len(data) < 1)
while True:
    data = my_socket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(), end='')

# Close connection. Just like with files!
my_socket.close()

# We will rarely need to do this. This is more of a low level implementation of a socket
# Python has built in modules for HTTP protocol
