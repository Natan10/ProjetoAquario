import sys
import socket
import threading
import time
import pickle as p 
sys.path.append('./Classes')
from aquario import Aquario

host = ''
port = 5680
WAIT = 30

def config_socket(host,port):
  meia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  meia.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  meia.bind((host,port))
  return meia

#enviando status
def status():
  msg = ['data',aquario2.get_estado_aquario()]
  cliente.sendto(p.dumps(msg),('localhost',5000))
  threading.Timer(WAIT,status).start()


cliente = config_socket(host,port)
aquario2 = Aquario('Aquario2',comida = 15)

cliente.sendto(p.dumps(['1','aq2']),('localhost',5000))

#Se idetificando para o servidor
cliente.sendto(p.dumps(['1','aq2']),('localhost',5000))

funcoes = ['1:get_nome','2:get_estado_luz','3:get_qtd_comida','4:get_estado_filtro','5:get_estado_aquario','6:set_estado_luz','7:set_estado_comer','8:set_estado_addcomida']


print("Iniciando Aquario2...")
status()

while True:
  try: 
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)

    if data[1] == 'aq2' and data[2] == 'list':
      print(address) 

      msg = ['2',funcoes]

      cliente.sendto(p.dumps(msg),('localhost',5000))


    elif data[0] == '1' and data[1] == 'ping':
      print(address)
      msg = ['1','aq2']
      cliente.sendto(p.dumps(msg),('localhost',5000))

    elif data[1] == 'aq2' and data[2] in funcoes:
      aux = funcoes[funcoes.index(data[2])]
      #if aux ==  
      print(address)
      msg = ['2',getattr(aquario2,data[2])]
      cliente.sendto(p.dumps(msg),('localhost',5000)) 


      if data[2] == '1':
        msg = ['2',aquario2.nome]
        cliente.sendto(p.dumps(msg),('localhost',5000)) 
      
      elif data[2] == '2':
        msg = ['2',aquario2.get_estado_luz()]
        cliente.sendto(p.dumps(msg),('localhost',5000))
      
      elif data[2] == '3':
        msg = ['2',aquario2.get_qtd_comida()]
        cliente.sendto(p.dumps(msg),('localhost',5000))

      elif data[2] == '4':
        msg = ['2',aquario2.get_estado_filtro()]
        cliente.sendto(p.dumps(msg),('localhost',5000))
      
      elif data[2] == '5':
        msg = ['2',aquario2.get_estado_aquario()]
        cliente.sendto(p.dumps(msg),('localhost',5000))

      elif data[2] == '6' and not(not data[3]):
        aquario2.set_estado_luz(int(data[3]))
        msg = ['2',aquario2.luz]
        cliente.sendto(p.dumps(msg),('localhost',5000))

      elif data[2] == '7' and not(not data[3]):
        aux = aquario2.set_estado_comer(int(data[3]))
        if not aux:
          msg = ['2',aquario2.get_qtd_comida()]
        else:
          msg = ['2',aux]

        cliente.sendto(p.dumps(msg),('localhost',5000))

      
      elif data[2] == '8' and not(not data[3]):
        aquario2.set_estado_addcomida(int(data[3]))
        msg = ['2',aquario2.comida]

        cliente.sendto(p.dumps(msg),('localhost',5000))

  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando Aquario2...")
    break    
