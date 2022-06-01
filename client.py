from socket import *
serverIP = '0.0.0.0'
serverPort = 6789
fileName = "index.html"
request = "GET "+str(fileName)+" HTTP/1.1"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
clientSocket.send(request.encode())
returnFromSever = clientSocket.recv(4096)

while(len(returnFromSever)>0):
    print(returnFromSever.decode())
    returnFromSever = clientSocket.recv(4096)
clientSocket.close()