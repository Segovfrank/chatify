import socket
import select
import sys

msg_queue = []

#Generate random id for client
clientid = 1
clientSet = False

#Credentials to connect
credentials = "abc"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("App 2 Started")

if len(sys.argv) != 3:
    print ("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))
server.send(bytes(credentials, encoding='utf-8'))

while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            last_char = str(message)[-2]
            
            if clientSet == False:
                clientid = last_char
                clientSet = True
            
            
            print (message)
            msg_queue.append(message)
        else:
            message = sys.stdin.readline()
            message = str(clientid) + message
            server.sendall(message.encode('utf-8'))
            sys.stdout.write("<You> ")
            sys.stdout.write(message[1:len(message)])
            msg_queue.append(message[1:len(message)])
            sys.stdout.flush()
server.close()