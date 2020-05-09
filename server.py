import socket
from _thread import start_new_thread
import sys
from ErrorHandler import *
from patterns import ServerSubject, ClientObserver, Message

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
the first argument AF_INET is the address domain of the socket. This is used when we have an Internet Domain
with any two hosts
The second argument is the type of socket. SOCK_STREAM means that data or characters are read in a continuous flow
"""
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if len(sys.argv) != 4:
    logging.error("Correct usage: script, IP address, port number, key")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server_key = str(sys.argv[3]).strip()
server.bind((IP_address, Port))
# binds the server to an entered IP address and at the specified port number. The client must be aware of these parameters
server.listen(100)
# listens for 100 active connections. This number can be increased as per convenience
list_of_clients = []
serverSubject = ServerSubject()
clientCounter = 0
clients = []


def clientthread(conn, addr):
    conn.sendall(b"Welcome to this chatroom! Your id is " + bytes(str(clients[clientCounter - 1].id), encoding='utf8'))
    # sends a message to the client whose user object is conn
    while True:
        try:

            message = str(conn.recv(2048))

            if message:
                messageCleared = message[3:(len(message) - 3)]
                clientId = int(message[2])
                logging.info(f"Client({clientId}) sent message: {messageCleared}")
                print("server received msg from client: ", clientId)
                serverSubject.send_message(Message(clientId, message))
                broadcast(bytes(f"from client ({clientId}) : {messageCleared}", encoding='utf-8'), conn)
                # prints the message and address of the user who just sent the message on the server terminal
            else:
                try:
                    remove(conn)
                except Exception as e:
                    print(f"Error removing connection: {e}")
                    continue
        except:
            continue


def broadcast(message, connection):
    for c in list_of_clients:
        if c != connection:
            try:
                c.send(message)
            except Exception as ex:
                broadCastError()
                c.close()
                remove(c)


def remove(connection):  # base component
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()

    client_key = str(conn.recv(16384))
    client_key = client_key[2:len(client_key) - 1]

    if client_key != server_key:
        connectionError()
    else:
        print("Client key: ", client_key)

        """
        Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
        the IP address of the client that just connected
        """
        print("Just for testing...server key: ", server_key)
        list_of_clients.append(conn)
        clients.append(ClientObserver(clientCounter, addr, conn, "abc"))
        serverSubject.attach(clients[clientCounter])

        print(addr[0] + " connected, your id is: " + str(clients[clientCounter].id))
        logging.warning(f"Client({str(clients[clientCounter].id)}) connected with ip {addr}")
        clientCounter = len(clients)

        # maintains a list of clients for ease of broadcasting a message to all available people in the chatroom
        # Prints the address of the person who just connected
        start_new_thread(clientthread, (conn, addr))
        # creates and individual thread for every user that connects

conn.close()
server.close()
