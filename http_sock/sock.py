import socket

sock = socket.socket()          # create socket
sock.bind(('localhost', 9090))           # split socket and port
sock.listen(1)                  # listen mode and max connect
conn, addr = sock.accept()       # get connect and create client connection

while True:
    data = conn.recv(1024)      # get data method 1kb
    if not data:
        break
    conn.send(data.upper())     # вернем клиенту данные в верхнем ригистре для примера

conn.close()                    # close connect

