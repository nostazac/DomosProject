import socket


addr = '100.130.41.175'
port = 20

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

result = socket_obj.connect_ex((addr, port))

socket_obj.close()