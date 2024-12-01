import socket

c = socket.socket()

c.connect(('localhost',9999))
print(c.recv(1024))
# it will print recived packets and 1024 is size of packets
