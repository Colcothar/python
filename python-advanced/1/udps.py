# UDP Server process for client in udpc.py
from socket import *
import re
serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('localhost',serverPort))
print("The server is ready....")
while(True):
	message,clientAddress= serverSocket.recvfrom(10000)
	msg=message.decode('utf-8')
	modf_msg=re.findall(r'\w+',msg)

        
	print("in server : ",tuple(modf_msg))
	print('op is ',modf_msg[1])
	if modf_msg[1]=='rev':
		resp=(modf_msg[0])[::-1]
	elif modf_msg[1]=='cap':
		resp=(modf_msg[0]).upper()
	elif modf_msg[1]=='encr':
		
		s=''
		for i in (modf_msg[0]):
			x=ord(i)+1
			s+=chr(x)

		resp=s
	else:
		resp="Invalid operation"
	serverSocket.sendto(resp.encode(('utf-8')),clientAddress)
	
