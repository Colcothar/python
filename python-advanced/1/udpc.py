# UDP client
from socket import *
import time

serverPort=12000
serverName='localhost'
clientSocket=socket(AF_INET,SOCK_DGRAM)
while(True):
	msg=input('Please enter input')
	op=input('please enter operation: ')
	#clientSocket.setdefaulttimeout(10)
	message=(msg,op)
	if message[0]=='exit':
		break
	clientSocket.sendto(str(message).encode('utf-8'),(serverName,serverPort))
	modf_msg,serverAddress=clientSocket.recvfrom(2048)
	print('result in client: ',modf_msg.decode())
	print("------------------------------------------------------------")
print("client closing...")
clientSocket.close()
print("client closed")
