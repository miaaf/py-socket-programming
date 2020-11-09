a = 1

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))
clientsocket, address = s.accept()

while a == 1:
 message = input("What is your message to server? : ")
 clientsocket.send(bytes(message, "utf-8"))
 print("Your message is succesfully sended!")
 msg = s.recv(1024)
 print(msg.decode("utf-8"))
 continue
