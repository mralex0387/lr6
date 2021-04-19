import socket

IP = '127.0.0.1'
PORT = 1005
buffersize = 65535

s = socket.socket()
s.connect((IP, PORT))
print("Соединение с сервером " + IP + ":" + str(PORT) + " установлено.\n")

while True:



    data = input("Введите a, operand, b через пробел: ").replace(" ", chr(0))
    pckSend = chr(0) + data
    s.send(bytearray(pckSend, 'utf-8'))
    pckRecv = s.recv(buffersize).decode("utf-8")
    if pckRecv == "ZeroDivisionError":
        print("Ошибка: деление на 0")
    else:
        print(pckRecv)

    print()

s.close()
print("Соединение закрыто.")