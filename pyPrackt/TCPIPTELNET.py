import socket

serv_sock = socket.socket(socket.AF_INET,           # Задаем семейство протоколов 'Интернет' (INET)
                          socket.SOCK_STREAM,       # Задаем тип передачи данных 'Потоковый' (TCP)
                          proto=0)                  # Выбираем протокол 'по умолчанию' для TCP, т.е. IP
print(type(serv_sock))

serv_sock.bind(('127.0.0.1', 53210))                # Чтобы привязать сразу ко всем адаптерам созданный сокет - ''
serv_sock.listen(10)                                # 10 - размер очереди входящих соединений

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:                                         # Чтение и запись данных в клиентский сокет
        data = client_sock.recv(1024)
        if not data:
            break
        client_sock.sendall(data)

    client_sock.close()