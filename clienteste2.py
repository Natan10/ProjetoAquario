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

cliente.sendto(p.dumps(['1','aq2']),('',5000))

funcoes = ['get_nome','get_estado_luz','set_estado_luz','get_qtd_comida','set_estado_comer','set_estado_addcomida','get_estado_filtro']
func = ['nome','comida','luz']

print("Iniciando Aquario2...")
while True:
  try:
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)

    if data[1] == 'aq2' and data[2] == 'list':
      print(address) 
      msg = ['2',func]
      cliente.sendto(p.dumps(msg),('',5000))

    elif data[0] == '1' and data[1] == 'nd':
      print(address)
      msg = ['1','aq2']
      cliente.sendto(p.dumps(msg),('',5000))

    elif data[1] == 'aq2' and data[2] in funcoes: 
      print(address)
      msg = ['2',getattr(aquario2,data[2])]
      cliente.sendto(p.dumps(msg),('',5000)) 

  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando Aquario2...")
    break    
