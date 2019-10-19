import sys
import socket
import time
import pickle as p 
sys.path.append('./Classes')
from portao import Portao

host = 'localhost'
port = 5680
lembrete = 0 

def config_socket(host,port):
  meia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  meia.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  meia.bind((host,port))
  return meia


cliente = config_socket(host,port)
portao = Portao('portao')

#Se idetificando para o servidor
cliente.sendto(p.dumps(['1','portao1']),('localhost',5000))
funcoes = ['1:get_nome','2:get_estado_portao','3:set_estado_portao']

time.sleep(2)
cliente.sendto(p.dumps('pt1'),('localhost',5000))
funcoes = ['1:get_nome','2:get_estado_portao','3:set_estado_portao']


print("Iniciando Portao1...")
while True:
  try:
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)
    if(lembrete)
      if(time.time() - lembrete > 10):
        msg = ['2',"O portão está aberto!"]
        cliente.sendto(p.dumps(msg),('localhost',5000))

    if data[1] == 'portao1' and data[2] == 'list':
      print(address) 
      msg = ['2',funcoes]
      cliente.sendto(p.dumps(msg),('localhost',5000))

    elif data[0] == '1' and data[1] == 'ping':
      print(address)
      msg = ['1','portao1']
      cliente.sendto(p.dumps(msg),('localhost',5000))

    elif data[1] == 'portao1':
      print(address)
      if data[2] == '1':
        msg = ['2',portao.nome]
        cliente.sendto(p.dumps(msg),('localhost',5000)) 
      
      elif data[2] == '2':
        if(portao.get_estado_portao()):
          estado = "Fechado"
        else:
          estado = "Aberto"
        msg = ['2',estado]
        cliente.sendto(p.dumps(msg),('localhost',5000))
      
      elif data[2] == '3':
        msg = ['2',portao.set_estado_portao()]
        if(portao.get_estado_portao()):
          lembrete = time.time()
        else: 
          lembrete = 0         
        cliente.sendto(p.dumps(msg),('localhost',5000))
               

   
  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando Aquario1...")
  break    
