import sys
import socket
import time
import pickle as p 

sys.path.append('../Funcoes')
sys.path.append('../Classes')
from luz import Luz
from funcoes import *

host = ''
port = 5680


cliente = config_sensor(host,port)
luz = Luz('Lampada')

#Se idetificando para o servidor
cliente.sendto(p.dumps(['1','lamp']),('',5000))
funcoes = ['1:get_nome','2:get_estado_luz','3:set_estado_luz']
validacao = ['1','2','3']

print("Iniciando Lampada...")

while True:
  try: 
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)

    if data[1] == 'lamp' and data[2] == 'list':
      print(address) 
      msg = ['2',funcoes,'lamp']
      cliente.sendto(p.dumps(msg),('',5000))

    elif data[0] == '1' and data[1] == 'ping':
      print(address)
      msg = ['1','lamp']
      cliente.sendto(p.dumps(msg),('',5000))

    elif data[1] == 'lamp':
      print(address)

      if data[2] not in validacao:
        msg = ['2','funçao inexistente','lamp']
        cliente.sendto(p.dumps(msg),('',5000))
      else:
        if data[2] == '1':
          msg = ['2',luz.nome,'lamp']
          cliente.sendto(p.dumps(msg),('',5000)) 
        
        elif data[2] == '2':
          msg = ['2',luz.get_estado_luz(),'lamp']
          cliente.sendto(p.dumps(msg),('',5000))
        
        elif data[2] == '3':
          msg = ['2',luz.set_estado_luz(),'lamp']
          cliente.sendto(p.dumps(msg),('',5000))

        elif data[2] == '4':
          msg = ['2',luz.get_tempo_ligada(),'lamp']
          cliente.sendto(p.dumps(msg),('',5000))

  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando Lampada...")
    break    
