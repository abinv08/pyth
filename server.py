import socket 
 
s = socket.socket() 
s.bind(("localhost", 5003)) 
s.listen(1) 
 
c, addr = s.accept() 
 
while True: 
    data = c.recv(1024) 
    if not data: 
        break 
    c.send(data)   # echo back 
 
c.close() 