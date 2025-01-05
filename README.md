# Client-Server Networking

Implementation of client-server communication models using TCP and UDP protocols. The project highlights the differences between connection-oriented and connectionless architectures.

## Table of Contents

- [Client-Server Networking](#client-server-networking)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Directory Structure](#directory-structure)
  - [Key Features](#key-features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Running TCP Server and Client](#running-tcp-server-and-client)
    - [Running UDP Server and Client](#running-udp-server-and-client)
  - [Learning Objectives](#learning-objectives)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Introduction

This project is designed to help understand the differences between TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) by implementing simple client-server applications for both protocols. The project includes:

1. A TCP server and client.
2. A UDP server and client.
3. Scenarios to compare the performance and behavior of TCP and UDP.

## Directory Structure

- `README.md`: Project documentation.
- `LICENSE`: License information.
- `tcp-udp_sockets/`: Directory containing the TCP and UDP client and server scripts.
  - `tcp_client.py`: TCP client implementation.
  - `tcp_server.py`: TCP server implementation.
  - `udp_client.py`: UDP client implementation.
  - `udp_server.py`: UDP server implementation.
## Key Features

- TCP Server: Listens for incoming connections and echoes received messages.
- TCP Client: Connects to the TCP server and exchanges messages.
- UDP Server: Listens for incoming messages and echoes them back.
- UDP Client: Sends messages to the UDP server and receives responses.

## Requirements

- Python 3.x
- A basic understanding of networking concepts is helpful but not mandatory.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Nylls241/client-server-networking.git
   cd client-server-networking
   ```
2. Install any required dependencies (if applicable).

## Usage 
### Running TCP Server and Client

1. Start the TCP server:
```sh
python3 tcp_server.py
```
2. Run the TCP client in a separate terminal:
```sh
python3 tcp_client.py
```

### Running UDP Server and Client
1. Start the UDP server:
```sh
python3 udp_server.py
```
2. Run the UDP client in a separate terminal:
```sh
python3 udp_client.py
```
## Learning Objectives

The aim of this project is to be able to program applications based on the client/server model
using the TCP and UDP transport layer protocols.

## License
This project is licensed under the terms of the [LICENSE](#LICENSE) file in this repository.

## Acknowledgments

I'd particularly like to thank my network architecture teacher for this project, which enabled us to apply the concepts we'd learned in class in a practical way.