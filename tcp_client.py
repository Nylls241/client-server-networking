# Echo client program
import socket

HOST = 'localhost'   # The remote host
PORT = 50007              # The same port as used by the server

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)
    print('Received', repr(data))
except Exception as e:
    print(f"An error occurred: {e}")