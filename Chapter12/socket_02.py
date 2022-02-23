import socket
import time

# socket instantiation
HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    # if un-commented --> we would get exactly 5120 bytes per loop.
    # time.sleep(0.25) gives the server to "get ahead" with the send request
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

# Close connection
mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")  # Busco el final del header (blank line), el pincipio de la información.
print('Header length', pos)
print(picture[:pos].decode())  # get the HEADER

# Skip past the header and save the picture data
picture = picture[pos+4:]  # get ONLY the image. Notice the slicing
# write picture to file.
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()