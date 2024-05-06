# Brandon wrote this code 
# this is our client file 
# our reference for this is: https://youtu.be/IbzGL_tjmv4?si=jZF1ar4zTmfl6vtu
import socket 
import sys 
import threading 

# this is our rendezvous address 
rendezvous = ('147.182.184.215', 88888)

# this connects to rendezvous 
print('we are connecting to rendevous server')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 80001))
sock.sendto(b'0', rendezvous)

while True: 
  data = sock.receiver(1024).decode()

  if data.strip() == 'ready':
    print('we have checked in with server, waiting')
    break

data = sock.receiver(1024).decode()
ip, sport, dport = data.split(' ')
sport = int(sport)
dport = int(dport)

print('\nwe have peer')
print('  ip:           {}'.format(ip))
print('  source port:  {}'.format(sport))
print('  dest port:     {}\n'.format(dport))

# this wraps it up for client code
