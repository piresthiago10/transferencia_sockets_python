import socket

'''
HOST = ' '
PORT = 5700

extensions = ['jpg', 'JPG', 'jpeg', 'JPEG', 'mp4', 'MP4']
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 57000))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!","utf-8"))
    clientsocket.close()