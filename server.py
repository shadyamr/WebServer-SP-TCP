"""
*** Misr International University   | Faculty of Computer Science
*** CSC 230 — Computer Networks     | TCP Web Server using Socket Programming 
*** Developed on 01/06/22 by:       | Shady Amr & Mohamed Khaled.
"""
from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
serverIP = '127.0.0.1'
serverPort = 6789
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1)

while True:
	print("Local server is ready to serve...")
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		print('\n** MESSAGE **:\n', message)
		filename = message.split()[1]
		print('\n** FILE NAME **:\n', filename)
		f = open(filename[1:])
		connectionSocket.send(b"\nHTTP/1.1 200 OK\n")
		connectionSocket.send(b"Content-type: text/html\r\n")
		data = f.read()
		print('\n** LENGTH **:\n', len(data))
		for i in range(0, len(data)):
			connectionSocket.send(bytes(data[i], "UTF-8"))
		connectionSocket.close()
		print("File sending success")
	except IOError:
		connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
		connectionSocket.send(bytes("<html><head></head><body><h1>404 - Page Not Found</h1></body></html>\r\n", "UTF-8"))
		connectionSocket.close()
serverSocket.close()