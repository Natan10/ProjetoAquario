import sys
import socket
import threading
import time
import pickle as p 
sys.path.append('./Classes')
from luz import Luz

host = ''
port = 5680


def config_socket(host,port):
  meia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  meia.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  meia.bind((host,port))
  return meia



cliente = config_socket(host,port)
luz = Luz('Lampada')

#Se idetificando para o servidor
cliente.sendto(p.dumps(['1','lamp1']),('',5000))
funcoes = ['1:get_nome','2:get_estado_luz','3:set_estado_luz']


print("Iniciando Lampada...")

while True:
  try: 
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)

    if data[1] == 'lamp1' and data[2] == 'list':
      print(address) 
      msg = ['2',funcoes]
      cliente.sendto(p.dumps(msg),('',5000))

    elif data[0] == '1' and data[1] == 'ping':
      print(address)
      msg = ['1','lamp1']
      cliente.sendto(p.dumps(msg),('',5000))

    elif data[1] == 'lamp1':
      print(address)
      if data[2] == '1':
        msg = ['2',luz.nome]
        cliente.sendto(p.dumps(msg),('',5000)) 
      
      elif data[2] == '2':
        msg = ['2',luz.get_estado_luz()]
        cliente.sendto(p.dumps(msg),('',5000))
      
      elif data[2] == '3':
        msg = ['2',luz.set_estado_luz()]
        cliente.sendto(p.dumps(msg),('',5000))

  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando Aquario2...")
    break    
