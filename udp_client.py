"""
UDP Client Program

This script creates a UDP client socket, sends a message to a UDP server,
and receives a response from the server.
"""
# Echo client program
import socket

HOST = 'localhost'  # The remote host
PORT = 50008        # The same port as used by the server

try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # Create a socket object
        data, server = s.recvfrom(1024)  # Receive data from the server
    print('Received', repr(data))  # Print the received data
except Exception as e:
    print(f"An error occurred: {e}")