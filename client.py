import socket

HOST = '127.0.0.1'  # IP du serveur
PORT = 5000  # Port du serveur


def main():
    # 1) Créer un socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"Client est prêt à discuter avec le serveur {HOST}:{PORT}.")

    try:
        while True:
            # 2) Saisir le message côté client
            message_client = input("Client : Tapez votre message (ou 'exit' pour quitter) : ")

            # - Envoyer le datagram au serveur
            client_socket.sendto(message_client.encode('utf-8'), (HOST, PORT))

            if message_client.lower() == 'exit':
                print("Client : Fermeture du client (exit).")
                break

            # 3) Recevoir la réponse du serveur
            data, server_addr = client_socket.recvfrom(1024)
            message_serveur = data.decode('utf-8')

            if message_serveur.lower() == 'exit':
                # Le serveur a envoyé "exit", il se ferme
                print("Client : Le serveur a tapé 'exit'. Fin de la communication.")
                break

            print(f"[Client : Réponse du serveur : {message_serveur}")

    finally:
        # 4) Fermer le socket
        client_socket.close()
        print("Client : Socket fermé. Au revoir !")


if __name__ == "__main__":
    main()
