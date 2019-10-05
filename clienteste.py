import sys
import socket
import pickle as p 
sys.path.append('./Classes')
from aquario import aquario


host = ''
port = 5680

meia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
meia.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 2)
meia.bind((host,port))


aquario1 = aquario('Aquario1',comida = 10)

while True:
  data,address = meia.recvfrom(1024)
  print("Address: {}\n".format(address))
  data = p.loads(data)

  if data == 'aquario1':
    msg = p.dumps(aquario1.get_nome())
    meia.sendto(msg,address)

  print("Mensagem enviada!")
  