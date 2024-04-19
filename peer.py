# JD wrote this code
import socket
import threading
import time

class Peer:
    def __init__(self, host, port):
        # Initialize the Peer object with host address and port number
        self.host = host
        self.port = port
        # Create a socket object using TCP/IP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # List to keep track of connections
        self.connections = []
        
    def connect(self, peer_host, peer_port):
        # Try to establish a connection to another peer
        try:
            connection = socket.create_connection((peer_host, peer_port))
            self.connections.append(connection)  # Add the connection to the list
            print(f"Connected to {peer_host}:{peer_port}")
        except socket.error as e:
            # Handle exceptions during connection attempt
            print(f"Failed to Connect {e}")

    def listen(self):
        # Bind the socket to the host and port and start listening for connections
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)  # Listen for connections, max 10 queued connections
        print("Listening for connections")

        while True:
            # Accept any new connections and start a new thread to handle the client
            connection, address = self.socket.accept()
            self.connections.append(connection)
            print(f"Accepted connection from {address}")
            threading.Thread(target=self.handle_client, args=(connection, address)).start()

    def send_data(self, data):
        # Send data to all connected peers
        for connection in self.connections:
            try:
                connection.sendall(data.encode())  # Send encoded string data
            except socket.error as e:
                # Handle possible socket errors during send
                print(f"Failed to send data {e}")
                self.connections.remove(connection)  # Remove the connection if it fails

    def handle_client(self, connection, address):
        # Handle the client connection
        while True:
            try:
                data = connection.recv(1024)  # Receive data from the client
                if not data:
                    break  # If no data, break the loop and end the thread
                received_message = data.decode()
                print(f"Received data from {address}: {received_message}")
                # Process commands sent by peers
                if received_message == "status":
                    status = f"Connected to {len(self.connections)} peers"
                    connection.send(status.encode())
                elif received_message.startswith("broadcast:"):
                    message = received_message.split(":", 1)[1]
                    self.send_data(message)
            except socket.error:
                # Handle possible socket errors
                break

    def keep_alive(self):
        # Send a keep-alive message every 10 seconds to all peers
        while True:
            time.sleep(10)
            self.send_data("keep_alive")

    def admin_commands(self):
        # Admin command processing loop
        while True:
            cmd = input("Enter command: ")
            if cmd == "shutdown":
                # Close all connections and the main socket on shutdown command
                for conn in self.connections:
                    conn.close()
                self.socket.close()
                break
            elif cmd == "list_connections":
                # Print the list of current connections
                print(self.connections)

    def start(self):
        # Start listening and admin command threads
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()
        keep_alive_thread = threading.Thread(target=self.keep_alive)
        keep_alive_thread.start()
        admin_thread = threading.Thread(target=self.admin_commands)
        admin_thread.start()

if __name__ == "__main__":
    # Example usage: Start two peers and establish a connection between them
    node1 = Peer("0.0.0.0", 8000)
    node1.start()

    node2 = Peer("0.0.0.0", 8001)
    node2.start()

    # Allow some time for nodes to start listening
    time.sleep(2)

    node2.connect("127.0.0.1", 8000)
    time.sleep(1)  # Allow connection to establish
    node2.send_data("Hello from node2!")
