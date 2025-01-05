# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
                          # Port to listen on (non-privileged ports are > 1023)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Create a socket object
        s.bind((HOST, PORT)) # Bind the socket to an IP address and port
        s.listen(1) # Listen for incoming connections
        print(f"Server listening on port {PORT}")
        conn, addr = s.accept() # Accept a connection from a client
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024) # Receive data from the client
                if not data: break # If no data is received, break the loop
                conn.sendall(data) # Send the received data back to the client
except Exception as e:
    print(f"An error occurred: {e}")