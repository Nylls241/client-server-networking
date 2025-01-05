import socket
import threading

HOST = '127.0.0.1'
PORT = 5001

def listen_for_messages(sock, running):
    """
    Dedicated thread for receiving UDP messages.

    Args:
        sock (socket): The UDP socket for communication.
        running (list): A shared flag to indicate if the thread should keep running.
    """
    while running[0]:
        try:
            data, addr = sock.recvfrom(1024)
            if not data:
                continue

            message = data.decode('utf-8')
            if message.lower() == 'exit':
                print("[Client] The server sent 'exit'. Ending communication.")
                running[0] = False
            else:
                print(f"[Client] Response from server: {message}")

        except OSError:
            break

def main():
    """
    Main function to start the UDP client. Handles user input and communication with the server.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"[Client] Ready to chat with {HOST}:{PORT}...")

    running = [True]

    # Thread to listen for server messages
    listener_thread = threading.Thread(
        target=listen_for_messages,
        args=(client_socket, running),
        daemon=True
    )
    listener_thread.start()

    try:
        while running[0]:
            message_client = input("[Client] Enter your message (or 'exit' to quit): ")
            client_socket.sendto(message_client.encode('utf-8'), (HOST, PORT))

            if message_client.lower() == 'exit':
                print("[Client] Exiting chat.")
                running[0] = False

    finally:
        client_socket.close()
        print("[Client] Socket closed. Goodbye!")

if __name__ == "__main__":
    main()
