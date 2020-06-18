import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send("hello, world!".encode())  # чтобы не получить ошибку , не забываем делать encode

data = sock.recv(1024)
sock.close()

print (data)