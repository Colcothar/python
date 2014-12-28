# TCP client
from socket import *
import re
import time

while(True):
	serverPort=12000
	serverName='localhost'
	clientSocket=socket(AF_INET,SOCK_STREAM)#c
	clientSocket.connect((serverName,serverPort))

	while(True):
		msg=input('Please enter input:(exit to quit) ')
		op=input('please enter operation: ')
		#clientSocket.setdefaulttimeout(10)
		message=(msg,op)
		if message[0]=='exit':
			break
		clientSocket.send(str(message).encode('utf-8'))
		modf_msg=clientSocket.recv(2048)
		print('result in client: ',modf_msg.decode())
		print("------------------------------------------------------------")
	print("client closing...")
	clientSocket.close()
	print("client closed")
