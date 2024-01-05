import socket
import ipaddress
import subprocess
import os

def scan_ports(target_ip, start_port, end_port):
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)
        
        sock.close()
        
    return open_ports

def run_nmap(target_ip):
    
    try:
        
        result = subprocess.check_output(["nmap", "-Pn", target_ip])
        return result.decode("utf-8")
    
    except subprocess.CalledProcessError as e:
        
        return f"Error: {e.output.decode('utf-8')}"
    
def main():
    
    target_ip = input("Enter  the IP address: ")
    start_port = int(input("Enterthr starting port: "))
    end_port = int(input("Enter the ending port: "))
                   
    # Validate the target IP address
    
    try:
        
        ipaddress.ip_address(target_ip)
        
    except ValueError:
        
        print("Invalid IP address. ")
        return
    open_ports = scan_ports(target_ip, start_port, end_port)
    print("\nScanning complete. Open ports: ", open_ports)
    
    nmap_result = run_nmap(target_ip)
    print("\nNmap Scan Result:\n", nmap_result)
    
if __name__ == "__main__":
    main()    