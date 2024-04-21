# Semester-Project
# Brandon Cazares, Meraj Nushin and JD Norris Group 5
# CECS 327 Sec 2 

# In this project, we're going to select a topic that relates to distributed network computing 

# Our selected topic is computer networking

# Our project should encompass software development, meticulous experimentation, and through analysis of outcomes. 

# If this is possible, we need to steer clear of naturally-distribution challenges; we must aim for something that presents a substantial complexity. 

# This is our approach: 
- For Computer Networking, we decided to research this topic because we were both interested how we're going to connect all nodes between Computer A and Computer B.
- Establishing these connections is going to allow users to communicate easily through the nodes.
- After these communications are established, they will determine if the nodes are successfully linked to our router, server, firewall and internet.

# This is our purpose: 
- The goal of this topic is to share resources through a reliable communication formed between multiple networks within a linked connection amongst each other.
- Another purpose of this project is to share different types of networks such as Local Area Network, Wide Area Network, Metropolitan Area Network, and Wireless Network. These networks enchance the communication with two or more nodes in which these will all be linked using wires to share data.
- We are trying to also understand the 7 layers of the OSI model have a very important purpose with computer networking and that it uses layers for visual representation of how a networking system functions. These layers have a protocol which can be interchanged very comfortably since model modifications don't influence other layers that change significantly.
- Cyber security has become such an important factor in everyday computer usage, yet there isn’t much research done on how to encrypt data across networks and we want to figure out how to do this. 

# This is our activity:
- Build a distributed system allowing multiple nodes to connect to a server.
- Allow these nodes to send messages between each other if successful. 
- Make an encryption method to secure messages sent from nodes.
- Have an encryption method send messages to see if nodes successfully went through.

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


