import sys
import socket
import time
import pickle as p 
sys.path.append('./Classes')
from portao import Portao

host = 'localhost'
port = 5680

def config_socket(host,port):
  meia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  meia.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  meia.bind((host,port))
  return meia


cliente = config_socket(host,port)
aquario1 = Portao('Portao1')

time.sleep(2)
cliente.sendto(p.dumps('pt1'),('localhost',5000))
funcoes = ['get_nome','get_estado_luz','set_estado_luz','get_qtd_comida','set_estado_comer','set_estado_addcomida','get_estado_filtro']
func = ['nome','estado']    

print("Iniciando Portao1...")
while True:
  try:
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)

    if data[0] == 'pt1' and data[1] == 'list':

      cliente.sendto(p.dumps(funcoes),('localhost',address))
    elif data[0] == 'pt1' and data[1] in funcoes:
      msg = getattr(aquario,data[1])
      cliente.sendto(p.dumps(msg),('localhost',address)) 
    elif data[0] == '1' and data[1] == 'nd':
      print(address)
      msg = ['1','pt1']
      cliente.sendto(p.dumps(msg),('localhost',5000))

  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando Aquario1...")
  break    
