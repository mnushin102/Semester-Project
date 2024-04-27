# Brandon wrote this code 
# this is our server file
# our reference for this is : https://youtu.be/IbzGL_tjmv4?si=jZF1ar4zTmfl6vtu
import socket 

# this is our known port address
known_port = 80002

# this is how we start our sockets 
sock = socket.socket(socket.AF_IFNET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 88888))

# we need to make two while loops which are both true because we need to test if the address is going to the server 
while True:
  clients = []

  while True:
    data, address = sock.recvfrom(128)
    # this will test our connection
    print('Connection from: {}' .format(address))
    clients.append(address)

    sock.sendto(b'ready', address)
    # this will check if both of our clients are ready 
    if len(clients) == 2:
        print('we have both clients ready, sending details to each')
        break

    # now, we need to create our clients 
    client1 = clients.pop()
    client1_address client1_port = client1
    client2 = clients.pop()
    client2_address client2_port = client2

    # finally, we need to test both our clients to see if they successfully sent a message from the server 
    sock.sendto('{} {} {}'.format(client1_address, client1_port, known_port).encode(), client2)
    sock.sendto('{} {} {}'.format(client2_address, client2_port, known_port).encode(), client1)
    

