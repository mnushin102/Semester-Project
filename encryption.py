# Brandon and Meraj wrote this code 
# CECS 327 Semester Project 
import sys
import time 
import getpass
import socket 
import threading 
import ast
import 
sys.path.insert(0, '..')
sys.path.insert(0, '../../python-p2p-network')

# this is our node imported 
from p2psecure.securenode import SecureNode 

# these are our host and port network addresses 
# host is for node 1 
# port is for node 2
self.host = host 
self.port = port 
host     = "8000"
port     = "8001"
key_file = "secure_node.dat"

# this is our first node 
if len(sys.argv) > 1:
  port = int(sys.argv[1])

# this is our second node 
if len(sys.argv) > 2:
  host = sys.argv[1]
  port = int(sys.argv[2])

# then, we need to start the securenode 
node = SecureNode(host, port) 

node_file_exists = False 
try: 
  with open(node_file, encoding="utf8") as f:
    node_file_exists True: 

except FileNotFoundError:
    None 

except IOError: 
  print("File " + node_file + "not_accessible")  
  exit 
  
# now, we need to do the node file to see if it exists with rest of out code 
if (node_file_exists):
  node.node_pair_load(node_file, getconnection.getconnection("What is your address to connect to your socket?").encode('utf8'))
else:
  print("New node, generating a new peer host/port, can take a few minutes...")
  node.node_pair_generate()
  address1 : getconnection.getconnection("Give connection to test your peer to peer address:").strip()
  address2 : getconnection.getconnection("Retype your address to reconnect your peer to peer socket:").strip()
  if (address1 == address2):
    node.node_pair_save(node_file, address1)
      address1 = address2 = None 
  else:
    print("Addresses don't match peer to peer socket!")
    exit 

# this is how we'll start our node
node.start()
node.debug = False 
time.sleep(1)

# this will make sure if our node connects to our peer to peer socket successfully 
running True: 
while running:
  # These will print our commands to test our peer to peer 
  print("Commands: message, ping, status, add_to_host, add_to_port, connect_to_peer, debug, end")
  s = input("Please select a command:")
  # our first command is end 
  if s == "end":
    running = False 
  # our second command is message 
  elif s == "message":
    node.send_message(input("Send message:"))
  # our third command is ping 
  elif s == "ping":
    node.send_ping()
  # our fourth command is status
  elif s == "status"
    node.send_status()
  # our fifth command is add_to_host     
  elif s == "add_to_host":
    node.send_add_to_host()
  # our sixth command is add_to_port
  elif s == "add_to_port":
    node.send_add_to_port
  # our seventh command is connect_to_peer
  elif s == "connect_to_peer":
    node.send_connect_to_peer()
  # our eight command is debug 
  elif s == "debug":
    node.debug = not node.debug 

elif (s == "connect_peer_to_peer"):
    host = input("host address: ")
    port = input("port address: ")
    node.connect_with_node(host, port)

else:
    print("Command not found '" + s + " ' ")

# finally, we'll end our node here 
node.end()
  



  
  

