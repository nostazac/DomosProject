import socket
target_host  = '192.168.22.19'
target_port = 80

#socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#connect client
client.connect((target_host,target_port))

#send some data
client.sendto("AAABBBCCC",(target_host, target_port))

#receive some data
data,addr = client.recvfrom(4096)

print (data)