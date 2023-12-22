# made a Client
'''
Clients receive and send data simutaniasly
'''
import socket
import threading # does things at the same time

# Choosing Nickname
alias = input("Choose your alias >>> ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            # Receive Message From Server
            # decode it and print
            message = client.recv(1024).decode('utf-8')
            #if message == 'ALIAS':
              #  client.send(alias.encode('utf-8'))
           # else:
            print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

def send():
    while True:
        message = '{}: {}'.format(alias, input(''))
        client.send(message.encode('utf-8'))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=send)
write_thread.start()