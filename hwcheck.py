import http.client  
host=input("Enter domain :")  
conn=http.client.HTTPConnection(host)  
conn.request("GET","/")  
res=conn.getresponse()       
print("Status :",res.status)  
 
if res.status==200:  
        print("Server is UP")  
else:  
        print("Server is DOWN") 