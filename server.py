"""
*** Misr International University   | Faculty of Computer Science
*** CSC 230 — Computer Networks     | TCP Web Server using Socket Programming 
*** Developed on 01/06/22 by:       | Shady Amr & Mohamed Khaled.
"""
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverIP = '0.0.0.0'
serverPort = 6789
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)

while True:
	print("Local server is ready to serve...")
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		print('\n** MESSAGE **:\n', message)
		filename = message.split()[1].decode('utf-8').strip("/")
		print('\n** FILE NAME **:\n', filename)
		f = open(filename[1:])
		outputdata = f.read()
		f.close()
		connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
		print('\n** LENGTH **:\n', len(outputdata))
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.send("\r\n")
		connectionSocket.close()
		print("File sending success")
	except IOError:
		connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
		connectionSocket.send(bytes("<html><head></head><body><h1>404 - Page Not Found</h1></body></html>\r\n", "UTF-8"))
		connectionSocket.close()
serverSocket.close()