import socket 
 
c = socket.socket() 
c.connect(("localhost", 5003)) 
 
msg = input("Enter message: ") 
c.send(msg.encode()) 
 
print("Echo:", c.recv(1024).decode()) 
 
c.close() 