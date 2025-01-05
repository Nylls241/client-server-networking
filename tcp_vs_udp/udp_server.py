import socket
import threading

HOST = '127.0.0.1'
PORT = 5001

def listen_for_messages(sock, running, client_addr):
    """
    Dedicated thread for receiving UDP messages.

    Args:
        sock (socket): The UDP socket for communication.
        running (list): A shared flag to control the loop.
        client_addr (list): A mutable container to store the last known client address.
    """
    while running[0]:
        try:
            data, addr = sock.recvfrom(1024)
            if not data:
                continue

            message = data.decode('utf-8')
            if message.lower() == 'exit':
                print("[Server] The client sent 'exit'. Ending communication.")
                running[0] = False
            else:
                print(f"[Server] Message received from {addr}: {message}")

            client_addr[0] = addr

        except OSError:
            break

def main():
    """
    Main function to start the UDP server. Waits for client messages and responds to them.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f"[Server] Listening on {HOST}:{PORT}...")

    running = [True]
    client_addr = [None]

    listener_thread = threading.Thread(
        target=listen_for_messages,
        args=(server_socket, running, client_addr),
        daemon=True
    )
    listener_thread.start()

    try:
        while running[0]:
            message_server = input("[Server] Enter your message (or 'exit' to quit): ")

            if client_addr[0] is not None:
                server_socket.sendto(message_server.encode('utf-8'), client_addr[0])
            else:
                print("[Server] No known client address to send the message to.")

            if message_server.lower() == 'exit':
                print("[Server] Shutting down.")
                running[0] = False

    finally:
        server_socket.close()
        print("[Server] Socket closed. Goodbye!")

if __name__ == "__main__":
    main()
