import socket  
host=input("Enter domain :")  
port=int(input("enter port :"))  
  
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.settimeout(5)  
  
result=s.connect_ex((host,port))  
  
if result == 0:  
        print("Server is UP")  
else:  
        print("Server is DOWN")  
  
s.close() 