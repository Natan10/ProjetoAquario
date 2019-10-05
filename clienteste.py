import sys
import socket
sys.path.append('./Classes')
from aquario import aquario


host = ''
port = 5680

meia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
meia.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
meia.bind((host,port))


aquario1 = aquario('Aquario1',comida = 10)
aquario2 = aquario('Aquario2',comida = 15)
aquario3 = aquario('Aquario1',comida = 9)

while True:
  data,address = recvfrom(1024).decode()
  print("Address: {}\n".format(address))

  if data[1] == 'aquario1':
    meia.sendto(aquario1.get_nome().encode(),address)
  if data[1] == 'aquario2':
    meia.sendto(aquario2.get_nome().encode(),address)
  if data[1] == 'aquario3':
    meia.sendto(aquario3.get_nome().encode(),address)
    
  print("Mensagem enviada!")
  