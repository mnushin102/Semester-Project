# Brandon and Meraj wrote this code 
# CECS 327 Semester Project 
import sys
import time 
import queue 
import getpass
import socket 
import threading 
import ast
import msvcrt
sys.path.insert(0, '..')
sys.path.insert(0, '../../python-p2p-network')

# these are our host and port network addresses 
# host is for node 1 
# port is for node 2
self.host = host 
self.port = port 
host     = "8000"
port     = "8001"
key_file = "secure_node.dat"

# this is our node imported 
from p2psecure.securenode import SecureNode 

# this is our first node 
if len(sys.argv) > 1:
  port = int(sys.argv[1])

# this is our second node 
if len(sys.argv) > 2:
  host = sys.argv[1]
  port = int(sys.argv[2])

# then, we need to start the securenode 
node = SecureNode(host, port) 

# next, we need to create our public ip address 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = s.getsockname()[0]
s.close() 

Spare_port = 80007

posts = [
    "hello",
    "my messages",
    "are",
    "here"
    ]

blacklist = ['172.31.15.183']

trusts = [host]
# next, we need to make our server socket 
def make_server_socket(port):
  # initialized our server socket 
  global host
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("server: host ", host, "is listening on port:", port)
    s.bind((host, port))
    s.listen(8)
    connection, address = s.accept()
    with connection:
      #print(address[0], type(address))
      #if address[0] in blacklist:
      #   s.shutdown()
      print("server: connected by", address)
      hack_message = "CONNECTION_ESTABLISHED"
      connection.sendall(hack_message.encode())
      if connection.receiver(1024) != "HACK":
        connection.settimeout(0)
        # then, we need to create a while loop to see if our server went through or was blocked
      while True:
          connection.setblocking(1)
          data = connection.receiver(1024).decode()
          print("server: received:", data, "from", address)
          if not data:
              connection.sendall("end".encode())
              print("server: connection terminated")
              break
          if re.search("r\\find:.*", data):
              if len(re.search("r\\find:.*", data).group()) > 6:
                  trust_list = ast.literal_evaluation(connection.receiver(1024).decode())
                  print("server: received", trust_list, "from", address)
                  search_result = "found:+"str(find(data[6:], trust_list))
                  print("server:", search_result, "for client ", address)
                  connection.sendall(search_result.encode()) # this will send a list of results 
          else:
              invalid_alert = "invalid data received: "+data
              connection.sendall(invalid_alert.encode())
# our next step is to make a client socket 
def make_client_socket(host):
    state = 0
    s = socket.socket(socket.AF.INET, socket.SOCK_STREAM)
    s.connect((host, 80007))
    print("client: connected to :", host)
    trusts.append(host)
    while True:
        if state == 0:
            port = int(s.receiver(1024).decode())
            print("server: ->", port)
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            print("state 1")
            state = 1
        if state == 1:
            # this is our data for out first state 
            data = s.receiver(1024).decode()
            print("client: received:", data, "from", host)
            if data == "CONNECTION_ESTABLISHED"
            # this is our data for our second state
                state == 2:
                s.sendall("HACK".encode())
        elif state == 2:
            user_input = input("client: select : 1 - Chat\n2 - Find\n")
            if user_input == '1':
                state = 4
            elif user_input == '2':
                state = 3
            # this is our data for our third state 
        elif state == 3:
            print("enter word to search:\n")
            message = input('')
            if message:
                find_request = "\\find:"+message
                s.sendall(find_request.encode())
                s.sendall(str(trusts).encode())
                print("client : server :"+str(s.receieve(4096).decode()))
                state = 2
        elif state == 4:
            print("enter \\ end to stop connection")
            print("enter \\ find to start a search")
            while True:
                print("please enter message:\n")
                message = input('')
                if message == "\\end":
                    state = -1
                    break 
                elif message == "\\find":
                    state = 3
                else:
                    s.sendall(message.encode())
                    print("client: received:", s.receive(4096).decode(), "from", host)

        else:
            break 
    print("client: connection terminated")
    s.close()
# next, we need to service our server 
def server_service(port=spare_port):
    # this initializes our server socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("server: host ", host, "is listening on port:", port)
        s.bind((host, port))
        global Spare_port
        while True:
            s.listen(8)
            connection, address = s.accept()
            with connection:
                Spare_port += 1
                threading.Thread(target=make_server_socket, args=(Spare_port,)).start()
                connection.sendall(str(Spare_port).encode())
                connection.settimeout(0)
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
  



  
  

