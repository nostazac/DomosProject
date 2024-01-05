import socket 
import cv2
import mss
import numpy as np

def share_screen(client_socket):
    with mss.mss() as sct:
        while True:
            frame = np.arrau(sct.shot())
            #encode the frame
            _, encode_frame = cv2.imencode(".jpg", frame)
            data = encode_frame.tobytes()
            
            #send the frame size first
            client_socket.send(str(len(data)).ljust(16).encode())
            
            
            
            #send the frame data
            client_socket.send(data)
            
server_ip = '0.0.0.0'
server_port = 8080

#create socket object
server_socket = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)

server_socket.bind((server_ip, server_port))

server_socket.listen(1)

print(f"[*]Server listening on {server_ip}:{server_port}")

client_socket, client_address = server_socket.accept()

print(f"[*] Connection established with {client_address}")

share_screen(client_socket)

client_socket.close()

server_socket.close()