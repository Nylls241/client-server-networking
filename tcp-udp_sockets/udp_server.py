"""
UDP Server Program

This script creates a UDP server socket, listens for incoming messages,
and echoes received messages back to the client.
"""
# Echo server program
import socket

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 50008  # Arbitrary non-privileged port

try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # Create a socket object
        s.bind((HOST, PORT))  # Bind the socket to an IP address and port
        print(f"Server listening on port {PORT}")
        while True:
            data, addr = s.recvfrom(1024)  # Receive data from the client
            print(f"Received message from {addr}: {data}")
            s.sendto(data, addr)  # Echo the data back to the client
except Exception as e:
    print(f"An error occurred: {e}")
