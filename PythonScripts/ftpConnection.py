import ftplib
def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.Login('BSIT/2021/47638','769795122')
		print("\n[*] "+ str(hostname)+"Login Success")
		ftp.quit()
		return True
	except:
		print ('\n[-] '+ str(hostname) + ' Login Failed')
		return False
host = "students.umma.ac.ke"
anonLogin(host)


