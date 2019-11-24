import sys
import socket
import time
import pickle as p 


sys.path.append('../Classes')
sys.path.append('../Funcoes')
from portao import Portao
from funcoes import *

host = ''
port = 5680



cliente = config_sensor(host,port)
portao = Portao('Portao')

#Se idetificando para o servidor
cliente.sendto(p.dumps(['1','port']),('',5000))
funcoes = ['1:get_nome','2:get_estado_portao','3:set_estado_portao']
validacao = ['1','2','3']


print("Iniciando Portão...")

while True:
  try: 
    data,address = cliente.recvfrom(1024)
    data = p.loads(data)

    if data[1] == 'port' and data[2] == 'list':
      print(address) 
      msg = ['2',funcoes,'port']
      cliente.sendto(p.dumps(msg),('',5000))

    elif data[0] == '1' and data[1] == 'ping':
      print(address)
      msg = ['1','port']
      cliente.sendto(p.dumps(msg),('',5000))

    elif data[1] == 'port':
      print(address)

      if data[2] not in validacao:
        msg = ['2','funçao inexistente','port']
        cliente.sendto(p.dumps(msg),('',5000))
      else:
        if data[2] == '1':
          msg = ['2','port','port']
          cliente.sendto(p.dumps(msg),('',5000)) 
        
        elif data[2] == '2':
          msg = ['2',portao.get_estado_portao(),'port']
          cliente.sendto(p.dumps(msg),('',5000))
        
        elif data[2] == '3':
          msg = ['2',portao.set_estado_portao(),'port']
          cliente.sendto(p.dumps(msg),('',5000))

  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Encerrando portão...")
    break    
