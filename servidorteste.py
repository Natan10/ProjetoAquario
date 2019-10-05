import socket 
import time
import pickle as p 


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 2)


server.settimeout(0.2)
server.bind(("", 44444))

msg = p.dumps("aquario1")

server.sendto(msg, ('<broadcast>', 5680))
time.sleep(1)
data,address = server.recvfrom(1024)
print(p.loads(data))
