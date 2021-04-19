import time
import socket
import threading

IP = '127.0.0.1'
PORT = 1005
backlog = 50
buffersize = 65535

s = socket.socket()
s.bind((IP, PORT))
s.listen(backlog)
print("Порт " + str(PORT) + " прослушивается...")


def new_connect(sock, addr):
    def send(pckData):
        sock.send(bytearray(pckData, 'utf-8'))

    last_message = chr(0)
    try:
        while True:
            data = sock.recv(buffersize).decode("utf-8")  # получаем данные
            if data == '': break
            a, operand, b = map(str, data[1:].split(chr(0)))  # коэффициенты разделены chr(0)
            try:
                if operand == "+":
                    f = int(a) + int(b)
                elif operand == "-":
                    f = int(a) - int(b)
                elif operand == "*":
                    f = int(a) * int(b)
                elif operand == "/":
                    f = int(a) / int(b)
                else:
                    send("Такой операции нет")
                send(str(f))
            except ZeroDivisionError:  # исключение деление на ноль
                send("ZeroDivisionError")
            print(addr[0] + " решить уравнение " + a + " " + operand + " " + b)
        sock.close()
        print("Соединение " + addr[0] + " закрыто")

    except Exception as e:
        sock.close()
        print(e)
        print(addr[0] + " исключение")
        print("Соединение " + addr[0] + " закрыто")


while True:
    sock, addr = s.accept()
    print("Новое соединение от " + addr[0])

    threading.Thread(target=new_connect, args=(sock, addr,)).start()  # создаем новый поток
