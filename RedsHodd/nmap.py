import nmap
def findTgts(subNet):
	nmScan = nmap.PortScanner()
	nmScan.scan(subNet, '445')
	tgtHosts = []
	print("<•> Gettin host")
	for host in nmScan.all_hosts():
 		if nmScan[host].has_tcp(445):
 			state = nmScan[host]['tcp'][445]['state']
 			if state == 'open':
 				print ('[+] Found Target Host: ' + host)
 				tgtHosts.append(host)
	return tgtHosts
findTgts('255.255.248.0')
