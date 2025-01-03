# Echo client program
import socket

HOST = 'localhost'   # The remote host
PORT = 50007              # The same port as used by the server

try: 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Create a socket object
        s.connect((HOST, PORT)) # Connect to the server
        s.sendall(b'Hello, world') # Send data to the server
        data = s.recv(1024) # Receive data from the server
    print('Received', repr(data)) # Print the received data
except Exception as e:
    print(f"An error occurred: {e}") 