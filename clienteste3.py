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
<<<<<<< Updated upstream
aquario1 = Portao('Portao1')
=======
luz = Luz('Lampada')

#Se idetificando para o servidor
cliente.sendto(p.dumps(['1','lamp1']),('localhost',5000))
funcoes = ['1:get_nome','2:get_estado_luz','3:set_estado_luz']
>>>>>>> Stashed changes

time.sleep(2)
cliente.sendto(p.dumps('pt1'),('localhost',5000))
funcoes = ['get_nome','get_estado_luz','set_estado_luz','get_qtd_comida','set_estado_comer','set_estado_addcomida','get_estado_filtro']
func = ['nome','estado']    

print("Iniciando Portao1...")
while True:
  try:
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)

<<<<<<< Updated upstream
    if data[0] == 'pt1' and data[1] == 'list':
=======
    if data[1] == 'lamp1' and data[2] == 'list':
      print(address) 
      msg = ['2',funcoes]
      cliente.sendto(p.dumps(msg),('localhost',5000))

    elif data[0] == '1' and data[1] == 'ping':
      print(address)
      msg = ['1','lamp1']
      cliente.sendto(p.dumps(msg),('localhost',5000))
>>>>>>> Stashed changes

      cliente.sendto(p.dumps(funcoes),('localhost',address))
    elif data[0] == 'pt1' and data[1] in funcoes:
      msg = getattr(aquario,data[1])
      cliente.sendto(p.dumps(msg),('localhost',address)) 
    elif data[0] == '1' and data[1] == 'nd':
      print(address)
<<<<<<< Updated upstream
      msg = ['1','pt1']
      cliente.sendto(p.dumps(msg),('localhost',5000))
=======
      if data[2] == '1':
        msg = ['2',luz.nome]
        cliente.sendto(p.dumps(msg),('localhost',5000)) 
      
      elif data[2] == '2':
        msg = ['2',luz.get_estado_luz()]
        cliente.sendto(p.dumps(msg),('localhost',5000))
      
      elif data[2] == '3':
        msg = ['2',luz.set_estado_luz()]
        cliente.sendto(p.dumps(msg),('localhost',5000))
>>>>>>> Stashed changes

  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando Aquario1...")
  break    
