# made a server

'''
Servers start, broadcast, and handle on client at a time all simutaniasly
'''

import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
aliases = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast('{} left!'.format(alias).encode('utf-8'))
            aliases.remove(alias)
            break

# Receiving / Listening Function
def start():
    while True:
        # Accept Connection
        print('Server is listening...')
        client, addr = server.accept()
        print(f"Connected with {addr}")

        # Request And Store Nickname
        client.send('Type your message'.encode('utf-8'))
        alias = client.recv(1024).decode('utf-8')
        aliases.append(alias)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Alias is {}".format(alias))
        broadcast("{} joined!".format(alias).encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == '__main__':
    start()