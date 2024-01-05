import socket
import threading

server_ip = '0.0.0.0'

server_port = 8000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((server_ip,server_port))
server.listen(0)
print("[*]Listening for connection on  %s:%d" %(server_ip,server_port))

client,addr = server.accept()

while True:
    request = client.recv(1024)
    request = request.decode("utf-8")
    
    if request.lower() == "close":
        client.send("Closed".encode("utf-8"))
        
        break
    print(f"Received: {request}")
    
    response = "accepted".encode("utf-8")
    
    client.close()
    print("Connection to Client closed")
    
    server.close()