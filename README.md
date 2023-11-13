# Simple Web server in Python

## Introduction

In the realm of web development, understanding the fundamentals of web servers is crucial. This article will guide you through the process of creating a basic web server in Python that can handle a single request. The server will be capable of establishing a connection with a client (browser), processing HTTP requests, retrieving requested files, and sending back a well-formed HTTP response. Additionally, we'll explore how to handle situations where the requested file is not found, returning a "404 Not Found" error message.

## Development Overview:

**Server Initialization:**

The server socket is created using the AF_INET address family and SOCK_STREAM socket type. The server then binds to a specified IP address and port.

**Connection Handling:**

The server enters an infinite loop, continuously listening for incoming connections. When a connection is established, it prints a message and proceeds to handle the request.

**Request Processing:**

The server receives and decodes the incoming HTTP request. It extracts the filename from the request to identify the requested resource.

**File Retrieval and Response Construction:**

The server attempts to open and read the requested file. If successful, it sends an HTTP header indicating success (status code 200 OK) and transmits the file content to the client.

<img width="960" alt="webserverpage" src="https://github.com/AfrahSaud36/WebServer/assets/138797663/9a40ed8a-6675-4839-a02c-6aa61637f10a">




**Error Handling:**

In case of an IOError (file not found), the server sends a "404 Not Found" HTTP response along with an HTML message indicating the error.

![web not](https://github.com/AfrahSaud36/WebServer/assets/138797663/0bb6cb18-f830-4fa2-9dbe-6ce5df4cd946)

**Connection Closure**

After processing the request, the server closes the connection.

## Python Code
```python
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
        connectionSocket.send("HTTP/1.1 404 Not found\r\n\r\n".encode())
        connectionSocket.send("<h1>“ 404 Not Found</h1>".encode())
        print('filenotfound')
        connectionSocket.close()
serverSocket.close()
sys.exit()

