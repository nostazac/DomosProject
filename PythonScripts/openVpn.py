import pyvpn


class OpenVpn:


    def vpnLogin():
        server_username = input("Username: ")
        server_password = input("Password: ")

    def fetch():
        server_ip = input("Enter server Ip: ")
        server_port  = int(input("Enter port: "))

        if server_ip < "1.1.1.1":
            print("Invalid ip")
        else:
            if server_port < 80:
                print("Invalid port number!")
            else:
                return True
            
    #def connection(username,password,encryption):
    
    def openVpn(self,server_ip,server_port):
        print("My openVp\n")
        print("Connecting to vpn on port: ",server_port)
        print("Server ip :",server_ip)

myobject = OpenVpn
myobject.fetch()
