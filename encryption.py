#Brandon and Meraj wrote this code 
import sys
import time 
import getpass
import socket 
import threading 
sys.path.insert(0, '..')
sys.path.insert(0, '../../python-p2p-network')

# this is our node imported 
from p2psecure.securenode import SecureNode 

# these are our host and port network addresses 
host     = "8000"
port     = "8001"
key_file = "secure_node.dat"

if len(sys.argv) > 1:
  port = int(sys.argv[1])

if len(sys.argv) > 2:
  host = sys.argv[1]
  port = int(sys.argv[2])

