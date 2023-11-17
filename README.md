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

![out finf](https://github.com/AfrahSaud36/WebServer/assets/138797663/edc7e051-9544-4bff-877b-2d56b56b4969)

![web found](https://github.com/AfrahSaud36/WebServer/assets/138797663/b6a627fc-fb5d-47c5-b7ad-00f48ce3581f)





**Error Handling:**

In case of an IOError (file not found), the server sends a "404 Not Found" HTTP response along with an HTML message indicating the error.

![out not find](https://github.com/AfrahSaud36/WebServer/assets/138797663/7a2df69a-ea4c-45bd-b657-b2718be0d2da)

![webnot](https://github.com/AfrahSaud36/WebServer/assets/138797663/7e35dae5-7497-4e33-bb2e-8d07fd892a81)


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
        connectionSocket.send("HTTP/1.1 oops file not found\r\n\r\n".encode())
        connectionSocket.send("<h1>“ 404 Not Found</h1>".encode())
        print('filenotfound')
        connectionSocket.close()
serverSocket.close()
sys.exit()

```

## Html Code
```html
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Hi</h1>
    <p> This is Afrah Saud assignment .</p>
</div>
</body>
</html>
```
