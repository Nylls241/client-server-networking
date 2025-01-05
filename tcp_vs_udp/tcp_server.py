import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def listen_for_messages(conn, running):
    """
    Dedicated thread for continuously receiving TCP messages.

    Args:
        conn (socket): The socket object representing the connection with the client.
        running (list): A shared flag to control the loop.
    """
    while running[0]:
        try:
            data = conn.recv(1024)
            if not data:
                print("[Server] The client has disconnected.")
                running[0] = False
                break

            message = data.decode('utf-8')
            if message.lower() == 'exit':
                print("[Server] The client sent 'exit'. Ending communication.")
                running[0] = False
            else:
                print(f"[Server] Message received: {message}")

        except ConnectionResetError:
            print("[Server] Connection interrupted (reset).")
            running[0] = False
            break

def main():
    """
    Main function to start the TCP server. Waits for client connections and handles communication.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"[Server] Listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    print(f"[Server] Client connected: {addr}")

    running = [True]

    # Thread to listen for client messages
    listener_thread = threading.Thread(
        target=listen_for_messages,
        args=(conn, running),
        daemon=True
    )
    listener_thread.start()

    try:
        while running[0]:
            message_server = input("[Server] Enter your message (or 'exit' to quit): ")
            conn.sendall(message_server.encode('utf-8'))

            if message_server.lower() == 'exit':
                print("[Server] Closing communication.")
                running[0] = False

    finally:
        conn.close()
        server_socket.close()
        print("[Server] Socket closed. Goodbye!")

if __name__ == "__main__":
    main()
