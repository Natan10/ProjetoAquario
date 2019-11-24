import sys
import socket
import threading
import time
import pickle as p 


sys.path.append('../Funcoes')
sys.path.append('../Classes')
from aquario import Aquario
from funcoes import *


host = ''
port = 5680
WAIT = 60


#enviando status
def status():
  msg = ['data',aquario.get_estado_aquario()]
  cliente.sendto(p.dumps(msg),('',5000))
  threading.Timer(WAIT,status).start()

cliente = config_sensor(host,port)
aquario = Aquario('Aquario',comida = 15)

#Se idetificando para o servidor
cliente.sendto(p.dumps(['1','aq']),('',5000))

funcoes = ['1:get_nome','2:get_estado_luz','3:get_qtd_comida','4:get_estado_filtro','5:get_estado_aquario','6:set_estado_luz','7:set_estado_comer','8:set_estado_addcomida']
validacao = ['1','2','3','4','5','6','7','8']

print("Iniciando Aquario...")
#status()

while True:
  try: 
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)

    if data[1] == 'aq' and data[2] == 'list':
      print(address) 
      msg = ['2',funcoes,'aq']
      cliente.sendto(p.dumps(msg),('',5000))

    elif data[0] == '1' and data[1] == 'ping':
      print(address)
      msg = ['1','aq']
      cliente.sendto(p.dumps(msg),('',5000))

    elif data[1] == 'aq':
      print(address)

      if data[2] not in validacao:
        msg = ['2','funçao inexistente','aq']
        cliente.sendto(p.dumps(msg),('',5000))
      else:
        if data[2] == '1':
          msg = ['2',aquario.nome,'aq']
          cliente.sendto(p.dumps(msg),('',5000)) 
        
        elif data[2] == '2':
          msg = ['2',aquario.get_estado_luz(),'aq']
          cliente.sendto(p.dumps(msg),('',5000))
        
        elif data[2] == '3':
          msg = ['2',aquario.get_qtd_comida(),'aq']
          cliente.sendto(p.dumps(msg),('',5000))

        elif data[2] == '4':
          msg = ['2',aquario.get_estado_filtro(),'aq']
          cliente.sendto(p.dumps(msg),('',5000))
        
        elif data[2] == '5':
          msg = ['2',aquario.get_estado_aquario(),'aq']
          cliente.sendto(p.dumps(msg),('',5000))

        elif data[2] == '6' and not(not data[3]):
          aquario.set_estado_luz(int(data[3]))
          msg = ['2',aquario.luz,'aq']
          cliente.sendto(p.dumps(msg),('',5000))

        elif data[2] == '7' and not(not data[3]):
          aux = aquario.set_estado_comer(int(data[3]))
          if not aux:
            msg = ['2',aquario.get_qtd_comida(),'aq']
          else:
            msg = ['2',aux,'aq']
          cliente.sendto(p.dumps(msg),('',5000))
        
        elif data[2] == '8' and not(not data[3]):
          aquario.set_estado_addcomida(int(data[3]))
          msg = ['2',aquario.comida,'aq']
          cliente.sendto(p.dumps(msg),('',5000))
          
  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando Aquario...")
    break    
