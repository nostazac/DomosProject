import socket
import threading
import sys
import signal

def send_messages(client_socket):
    while True:
        message  = input("You: ")
        client_socket.send(message.encode())
        
def receive_messages(client_socket):
    
    while True:
        message = client_socket.recv(1024).decode()
        print(f"Peer: {message}")
        
def main():
    host = '0.0.0.0'
    port = 8080
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    
    print("[*] Waiting for a peer to connect....")
    
    try:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        
        
        send_thread = threading.Thread(target=send_messages, args=(client_socket))
        receive_thread = threading.Thread(target=send_messages, args=(client_socket,))
        
        send_thread.start()
        
        receive_thread.start()
        
        
    except KeyboardInterrupt:
        print("[*]  Ctrl C pressed Exiting..")
        sys.exit(0)
    
if __name__ == "__main__":
    main()