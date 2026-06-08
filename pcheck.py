import socket

host = input("Enter host: ")
port = int(input("Enter port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

result = sock.connect_ex((host, port))

if result == 0:
    print(f"Port {port} is open")
else:
    print(f"Port {port} is not open")

sock.close()