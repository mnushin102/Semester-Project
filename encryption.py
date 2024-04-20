"Brandon and Meraj wrote this code" 
import sys
import time 
import getpass
import socket 
import threading 
sys.path.insert(0, '..')
sys.path.insert(0, '../../python-p2p-network')

from p2psecure.securenode import SecureNode 

host     = "8000"
port     = "8001"
key_file = "secure_node.dat"

if len(sys.argv) 
