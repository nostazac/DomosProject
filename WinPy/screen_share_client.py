import socket
import cv2
import numpy as np

server_ip = '192.168.34.106'
server_port = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_ip, server_port))

while True:
    # Receive the frame size
    
    frame_size = client_socket.recv(16)
    
    if not frame_size:
        
        # convert the frame size to integer
        frame_size = int(frame_size)
        
        # receive the data
        frame_data = client_socket.recv(frame_size)
        
        # Decode  the frame
        frame = cv2.imdecode(np.frombuffer(frame_data, np.unit8), cv2.IMREAD_COLOR)
        
        # diplay the received frame
        
        cv2.imshow("Screen Sharing", frame)
        
        # Check for key press to exit
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        

#release opencv window And close the connection when done

cv2.destroyAllWindows()
client_socket.close()