from socket import *
import sys 
serverSocket = socket(AF_INET, SOCK_STREAM)

ip = '########' # Your ip address
serverPort = 1234;
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("the server is ready to receive")

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:

        message= connectionSocket.recv(1024).decode()
        if message != '':
            print(message)
            filename = message.split()[1]
            print(filename)
            f = open(filename[1:])
            outputdata = f.read()
            f.close()
            print(type(outputdata))
            connectionSocket.send("HTTP/1.1 200 ok\r\n\r\n".encode())
            connectionSocket.send(outputdata.encode())
            connectionSocket.close()
          
    except IOError:
        connectionSocket.send("HTTP/1.1 oops file not found\r\n\r\n".encode())
        connectionSocket.send("<h1>“ 404 Not Found</h1>".encode())
        print('filenotfound')
        connectionSocket.close()
serverSocket.close()
sys.exit()
