import sys
import socket
import threading
import time
import pickle as p 
sys.path.append('./Classes')
from portao import Portao

host = 'localhost'
port = 5800
#lig = 0
#tempo_lig = 0
#tempo_total = 0

def config_socket(host,port):
  meia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  meia.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  meia.bind((host,port))
  return meia



cliente = config_socket(host,port)
portao = Portao('Portao')

#Se idetificando para o servidor
cliente.sendto(p.dumps(['1','pt11']),('localhost',5000))
funcoes = ['1:get_nome','2:get_estado_portao','3:set_estado_portao','4:get_tempo_ligada','5:get_tempo_total']


print("Iniciando Portao...")

while True:
  try: 
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)

    if data[1] == 'pt11' and data[2] == 'list':
      print(address) 
      msg = ['2',funcoes]
      cliente.sendto(p.dumps(msg),('localhost',5000))

    elif data[0] == '1' and data[1] == 'ping':
      print(address)
      msg = ['1','pt11']
      cliente.sendto(p.dumps(msg),('localhost',5000))

    elif data[1] == 'pt11':
      print(address)
      if data[2] == '1':
        msg = ['2',portao.nome]
        cliente.sendto(p.dumps(msg),('localhost',5000)) 
      
      elif data[2] == '2':
        msg = ['2',portao.get_estado_portao()]
        cliente.sendto(p.dumps(msg),('localhost',5000))
      
      elif data[2] == '3':
        msg = ['2',portao.set_estado_portao()]
        
        cliente.sendto(p.dumps(msg),('localhost',5000))
      
      elif data[2] == '4':
        msg = ['2', portao.get_tempo_ligada()]
        cliente.sendto(p.dumps(msg),('localhost',5000))
      
      elif data[2] == '5':
        msg = ['2',portao.att_tempo_total()]
        cliente.sendto(p.dumps(msg),('localhost',5000))                

  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando Aquario2...")
    break    