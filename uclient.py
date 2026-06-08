import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("You: ")

    c.sendto(msg.encode(), ("localhost", 12345))

    if msg.lower() == "exit":
        print("Chat ended.")
        break

    reply, _ = c.recvfrom(1024)
    reply = reply.decode()

    print("Server:", reply)

c.close()