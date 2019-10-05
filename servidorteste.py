import socket 
import time
import pickle as p 

def config_serve(host="",port=5000):
  server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  server.settimeout(0.2)
  server.bind((host, port))
  return server


servidor = config_serve()
msg = p.dumps("aquario1")

servidor.sendto(msg, ('<broadcast>', 5680))
time.sleep(1)
data,address = servidor.recvfrom(1024)
print(p.loads(data))
