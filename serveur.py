import socket

HOST = '127.0.0.1'  # Adresse IP locale
PORT = 5000  # Port UDP que le serveur écoute


def main():
    # 1) Créer le socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2) Associer (bind) le socket à l'adresse et au port
    server_socket.bind((HOST, PORT))

    print(f"Serveur en écoute sur le socket {HOST}:{PORT}...")

    try:
        # 3) Boucle principale d'échanges
        while True:
            # - Le serveur attend un message du client (data, client_addr)
            data, client_addr = server_socket.recvfrom(1024)

            if not data:
                # Si rien reçu (théoriquement peu probable en UDP), on quitte
                print(" Serveur : Aucune donnée reçue, fermeture.")
                break

            message_client = data.decode('utf-8')

            if message_client.lower() == 'exit':
                # Le client a signalé qu'il voulait quitter
                print("Serveur :Le client a tapé 'exit'. Fin de la communication.")
                break

            print(f"Serveur : Message reçu de {client_addr} : {message_client}")

            # 4) Le serveur répond en saisissant son message
            message_serveur = input("Serveur : Tapez la réponse (ou 'exit' pour quitter) : ")

            # - Envoyer la réponse au client
            server_socket.sendto(message_serveur.encode('utf-8'), client_addr)

            if message_serveur.lower() == 'exit':
                print("Serveur : Fermeture du serveur (exit).")
                break

    finally:
        # 5) Fermer le socket
        server_socket.close()
        print("Serveur : Socket fermé. Au revoir !")


if __name__ == "__main__":
    main()
