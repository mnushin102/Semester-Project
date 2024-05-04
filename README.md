# Semester-Project
# Brandon Cazares, Meraj Nushin and JD Norris Group 5
# CECS 327 Sec 2 

# In this project, we're going to select a topic that relates to distributed network computing 

# Our selected topic is Peer-to-Peer Modeling and Encryption. 

# Our project should encompass software development, meticulous experimentation, and through analysis of outcomes. 

# If this is possible, we need to steer clear of naturally-distribution challenges; we must aim for something that presents a substantial complexity. 

# This is our approach: 
- For Computer Networking, we decided to research this topic because we were interested in how we’re going to connect all nodes using P2P.
- A Peer-to-Peer model will let the nodes directly communicate with one another
- Establishing these connections allows nodes to send messages across a distributed and decentralized system.
- After these connections are established, we will sync the nodes, then implement and improve an encryption method to secure information sent across the system. 

# This is our purpose: 
- The goal of this topic is to share resources through a reliable communication formed between multiple networks within a linked connection amongst each other.
- To guarantee a reliable and safe way for the nodes to communicate we plan to use an encryption method to hide sensitive information and communication between preapproved nodes. 
- As decentralized models become more popular, we want to explore cyber security in a peer-to-peer model, we want to test and improve an encryption method that can be used for peer-to-peer systems. 

# This is our activity:
- Build a distributed system using peer-to-peer model allowing multiple nodes to connect to each other. 
- Allow these nodes to send messages between each other if successful. 
- Make an encryption method to secure messages sent from nodes.

Cyber security is getting more important as technology improves and we plan to investigate security protocols for distributed networks. This could include developing and implementing an encryption method, authentication protocols, or intrusion detection systems against unauthorized access.(or all 3).
 So we would have to set up our own distributed system that offers communication across nodes and have test cases for when someone is allowed to send a message or maybe turn on and off a node or create another. Maybe we can create some peer-to-peer model, can use network time protocol to synch all nodes to the same time, can use Machine queuing telemetry transport for messaging and develop something for node authentication, was looking at something called pki but didn't do too much research and some sort of detection system to see if certain nodes should exist, something that monitors the traffic on our distributed system and fix anomalies.

- Just wrote it here in case i can't explain it well enough - JD

We’re going to need to understand cyber security nowadays because distributed networks protocols have to do a lot with this. Encryptions are very well developed if done correctly using a method, authentication protocols or even intrusion detection systems against unauthorized access. In order to do this, we need to create our own distributed system from scratch by planning communication with enough nodes to send a message to the receiver. We’re going to come up with some plan here to figure out a connection to build a peer-to-peer model. In this case, we need to understand network protocols because peer-to-peer models can determine if all nodes are synced at once. Finally, machine querying can distinguish a connection between the network traffic from the nodes to the server if it’s done successfully. 

- Let me know if this is sufficient because i don’t know if this explains well regarding our plan - Brandon

Peer-to-peer model plan: 
Synch nodes using network time protocol.
Create code to figure out how to encrypt network time protocol.
Some sort of way to send messages maybe using machine queuing telemetry.
Can use PKI: public key infrastructure to manage a public-key encryption.
Allow two or more computers to connect and share resources without requiring a server. 
Use both computers to allow a successful connection to run.


These are our resources: 
https://www.irjmets.com/uploadedfiles/paper/volume3/issue_7_july_2021/14448/1628083561.pdf

Example on how to make a UDP based distributed system:
https://blog.devgenius.io/implementing-peer-to-peer-data-exchange-in-python-8e69513489af
Peer-to-peer (P2P) networks are decentralized systems where nodes, or peers, communicate and exchange data directly without relying on a central server. This architecture has become increasingly popular due to its ability to distribute data efficiently and handle large amounts of traffic.

Python is an excellent choice for implementing P2P networks due to its simplicity, readability, and extensive library support. This article will walk you through implementing a basic P2P data exchange system in Python.

Prerequisites

To follow this tutorial, you should have a basic understanding of Python programming and experience working with sockets, threads, and the standard library. Familiarity with basic networking concepts is also helpful.

Step 1: Installing Required Libraries

We will use the ‘socket’ library for networking and ‘threading’ for concurrent connections. Both libraries are part of the Python standard library, so no additional installation is needed.

Step 2: Defining the Peer Class

The first step in implementing our P2P network is to define a Peer class that will represent each node in the network. This class will handle creating and managing connections with peers and exchanging data.

import socket
import threading

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []
Step 3: Creating Connections

We’ll now define a method within our Peer class to create connections with other peers. This method will establish a connection to another peer’s IP address and port and add the new connection to the connections list.

    def connect(self, peer_host, peer_port):
        try:
            connection = socket.create_connection((peer_host, peer_port))
            self.connections.append(connection)
            print(f"Connected to {peer_host}:{peer_port}")
        except socket.error as e:
            print(f"Failed to connect to {peer_host}:{peer_port}. Error: {e}")
Step 4: Listening for Incoming Connections
We also need to allow our peers to accept incoming connections from other nodes. This can be achieved by defining a ‘listen’ method within the Peer class that binds the socket to the host and port and starts listening for incoming connections.

    def listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        print(f"Listening for connections on {self.host}:{self.port}")

        while True:
            connection, address = self.socket.accept()
            self.connections.append(connection)
            print(f"Accepted connection from {address}")
Step 5: Implementing Data Exchange
Now we’ll define a method for exchanging data between peers. This method will iterate through all connections and send data to each peer.

    def send_data(self, data):
        for connection in self.connections:
            try:
                connection.sendall(data.encode())
            except socket.error as e:
                print(f"Failed to send data. Error: {e}")
Step 6: Creating a Multithreaded Peer

Since we want our Peer class to be able to both listen for incoming connections and send data simultaneously, we need to implement multithreading. We will add a method to start the listening thread when the Peer class is initialized.

    def start(self):
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()
Step 7: Testing the P2P Network

Now it’s time to test our P2P network by creating two Peer instances and exchanging data.

Putting it all together


Here’s the full code implementation:

import socket
import threading

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []

    def connect(self, peer_host, peer_port):
        connection = socket.create_connection((peer_host, peer_port))

        self.connections.append(connection)
        print(f"Connected to {peer_host}:{peer_port}")

    def listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        print(f"Listening for connections on {self.host}:{self.port}")

        while True:
            connection, address = self.socket.accept()
            self.connections.append(connection)
            print(f"Accepted connection from {address}")
            threading.Thread(target=self.handle_client, args=(connection, address)).start()

    def send_data(self, data):
        for connection in self.connections:
            try:
                connection.sendall(data.encode())
            except socket.error as e:
                print(f"Failed to send data. Error: {e}")
                self.connections.remove(connection)

    def handle_client(self, connection, address):
        while True:
            try:
                data = connection.recv(1024)
                if not data:
                    break
                print(f"Received data from {address}: {data.decode()}")
            except socket.error:
                break

        print(f"Connection from {address} closed.")
        self.connections.remove(connection)
        connection.close()

    def start(self):
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()

# Example usage:
if __name__ == "__main__":
    node1 = Peer("0.0.0.0", 8000)
    node1.start()

    node2 = Peer("0.0.0.0", 8001)
    node2.start()

    # Give some time for nodes to start listening
    import time
    time.sleep(2)

    node2.connect("127.0.0.1", 8000)
    time.sleep(1)  # Allow connection to establish
    node2.send_data("Hello from node2!")
    
Video example:
https://www.youtube.com/watch?v=IbzGL_tjmv4&t=66s
Uses a rendezvous server for the nodes (or computers) to connect and share info on which is a bit different from peer-to-peer, but shows how to do peer-to-peer. Also, we will need to understand how this differs from peer-to-peer in several ways. 

With this set up, we need to establish a connection from peer-to-peer in order to check if our nodes went through our server and made sure peer-to-peer went through successfully. 

Create a menu system with commands 
Menu system can create a server and that server has options of sending or receiving a message and the option to encrypt or decrypt the message if they want
Research encryption method that doesn't have a lot of previous usage
Commands will help us how to create a menu system through powershell 

Article: https://www.cloudflare.com/learning/ssl/what-is-encryption/#:~:text=The%20two%20main%20kinds%20of,for%20both%20encryption%20and%20decryption.
https://www.codecademy.com/article/important-powershell-commands-for-cybersecurity-analysts
https://www.youtube.com/watch?v=FMnW4D4r_E4
https://support.workiva.com/hc/en-us/articles/360036005711-Encryption-commands




https://security.stackexchange.com/questions/107459/encryption-in-peer-to-peer-chat 

