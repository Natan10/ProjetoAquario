import sys
import socket
import pickle as p 
sys.path.append('./Classes')
from aquario import aquario


host = ''
port = 5680

def config_socket(host,port):
  meia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  meia.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  meia.bind((host,port))
  return meia


cliente = config_socket(host,port)
aquario1 = aquario('Aquario1',comida = 10)

while True:  
  data,address = cliente.recvfrom(1024)
  data = p.loads(data)
  if data == 'aquario1':
    print(f"Address:{address}")
    msg = p.dumps(aquario1.get_nome())
    cliente.sendto(msg,address)
    print("Mensagem enviada!")

  
  