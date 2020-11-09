anahtar = 1

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    while anahtar == 1:
     message = input("What is your message to server? : ")
     clientsocket.send(bytes(message, "utf-8"))
     print("Your message is succesfully sended!")
     msg = s.recv(1024)
     print(msg.decode("utf-8"))
     continue


