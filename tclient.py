import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 5001))

while True:
    msg = input("Client: ")
    c.send(msg.encode())

    if msg.lower() == "exit":
        break

    reply = c.recv(1024).decode()

    if not reply or reply.lower() == "exit":
        break

    print("Server:", reply)

c.close()