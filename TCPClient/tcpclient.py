import socket

target_host = "www.google.com"
target_port = 80

#create a socket object
#The AF_INET parameter is saying we are going to use a standard IPV4 address or hostname
#SOCK_STREAM indicates that this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send some data
#(code fixed) remember function client.send need bytes to send also need to encode.
client.send(bytes("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n", "utf-8"))

#recieve some data
response = client.recv(4096)

print(response)