import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def listen_for_messages(client_socket, running):
    """
    Dedicated thread for receiving TCP messages (client-side).

    Args:
        client_socket (socket): The client socket used for communication.
        running (list): A shared flag to indicate if the thread should keep running.
    """
    while running[0]:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("[Client] The server has closed the connection.")
                running[0] = False
                break

            message = data.decode('utf-8')
            if message.lower() == 'exit':
                print("[Client] The server sent 'exit'. Ending communication.")
                running[0] = False
            else:
                print(f"[Client] Message received from server: {message}")

        except ConnectionResetError:
            print("[Client] Connection interrupted (reset).")
            running[0] = False
            break

def main():
    """
    Main function to start the TCP client. Handles user input and communication with the server.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print(f"[Client] Connected to the server at {HOST}:{PORT}.")

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
            client_socket.sendall(message_client.encode('utf-8'))

            if message_client.lower() == 'exit':
                print("[Client] Exiting chat.")
                running[0] = False

    finally:
        client_socket.close()
        print("[Client] Socket closed. Goodbye!")

if __name__ == "__main__":
    main()
