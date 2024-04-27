# Brandon wrote this code 
# this is our server file
# our reference for this is : https://youtu.be/IbzGL_tjmv4?si=jZF1ar4zTmfl6vtu
import socket 

known_port = 80002

sock = socket.socket(socket.AF_IFNET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 88888))

while True:
  clients = []

  while True:
    data, address = sock.recvfrom(128)

    print('Connection from: {}' .format(address))
    clients.append(address)

    sock.sendto(b'ready', address)

    if len(clients) == 2:
        print('we have both clients ready, sending details to each')
        break

    # now, we need to create our clients 
    client1 = clients.pop()
    client1_address client1_port = client1
    client2 = clients.pop()
    client2_address client2_port = client2

    sock.sendto('{} {} {}'.format(client1_address, client1_port, known_port).encode(), client2)
    sock.sendto('{} {} {}'.format(client2_address, client2_port, known_port).encode(), client1)
    

