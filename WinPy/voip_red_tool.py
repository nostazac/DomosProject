from scapy.all import IP, UDP, RTP,sniff


def capture_voip_packets(target_ip, port):
    
    packets = sniff(filter = f"host {target_ip} and port {port}", count = 0)
    
    
    # Process captured packets
    for packet in packets:
        if RTP in packets:
            #Extract and print voip payload (audio data)
            voip_payload = packet[RTP].load.decode('ut-8', errors = 'ignore')
            print(f"\n VoIP Payload: \n{voip_payload}")
            
def main():
    target_ip  = input("Enter the target IP address: ")
    target_port = int(input("Enter the target Voip port: "))
    
    print("\nCapturing VoIP Packets...")
    capture_voip_packets(target_ip, target_port)
    
if __name__ == "__main__":
    main()