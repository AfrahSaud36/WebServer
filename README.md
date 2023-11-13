# Simple Web server in Python

##Introduction

In the realm of web development, understanding the fundamentals of web servers is crucial. This article will guide you through the process of creating a basic web server in Python that can handle a single request. The server will be capable of establishing a connection with a client (browser), processing HTTP requests, retrieving requested files, and sending back a well-formed HTTP response. Additionally, we'll explore how to handle situations where the requested file is not found, returning a "404 Not Found" error message.

## Development Overview:

**Connection Initialization**

Our web server begins its journey by creating a connection socket upon receiving a request from a client. This socket serves as the communication bridge between the server and the browser.

**Request Processing**

Once the connection is established, the server receives and processes the incoming HTTP request from the client. This step involves parsing the request to identify the specific file being sought.

**File Retrieval**

With the target file identified, the server accesses it from its file system. This step is crucial in determining the content that will be included in the HTTP response.

**HTTP Response Construction**

The server assembles an HTTP response message, including the requested file preceded by essential header lines. These headers convey vital information about the response, such as content type and length.

**Response Transmission:**

Following the response construction, the server transmits the HTTP response over the TCP connection back to the requesting browser. This action completes the communication cycle between the server and the client.

**Handling File Absence:**

To enhance the server's resilience, it checks for the existence of the requested file. If the file is not found, the server responds with a "404 Not Found" error message, signaling that the requested resource is unavailable.

![web not](https://github.com/AfrahSaud36/WebServer/assets/138797663/0bb6cb18-f830-4fa2-9dbe-6ce5df4cd946)

