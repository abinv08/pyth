import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 12345))

while True:
    msg, addr = s.recvfrom(1024)
    message = msg.decode()

    print("Client:", message)

    reply = input("You: ")

    s.sendto(reply.encode(), addr)

    if reply.lower() == "exit":
        print("Server ended the chat.")
        break

s.close()