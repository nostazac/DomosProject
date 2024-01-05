import socket
target_host  = '192.168.22.19'
target_port = 80

#socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect client
client.connect((target_host,target_port))

#send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print (response)