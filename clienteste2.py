import sys
import socket
import time
import pickle as p 
sys.path.append('./Classes')
from aquario import Aquario

host = ''
port = 5680



def config_socket(host,port):
  meia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  meia.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  meia.bind((host,port))
  return meia


cliente = config_socket(host,port)
aquario2 = Aquario('Aquario2',comida = 15)

time.sleep(2)
cliente.sendto(p.dumps('aq2'),('',5000))
funcoes = ['get_nome','get_estado_luz','set_estado_luz','get_qtd_comida','set_estado_comer','set_estado_addcomida','get_estado_filtro']
    

print("Iniciando Aquario2...")
while True:
  try:
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)
    if data[0] == 'aq2' and data[1] == 'list':
      cliente.sendto(p.dumps(funcoes),('',address))
    elif data[0] == 'aq2' and data[1] in funcoes:
      msg = getattr(aquario2,data[1])
      cliente.sendto(p.dumps(msg),('',address)) 
  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando Aquario2...")
  break    
