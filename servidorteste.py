import sys
import socket
import threading
import time
import pickle as p 

sys.path.append('./Classes')
from descoberta import Descoberta

host = ""
port = 5000

def config_serve(host="",port=5000):
  server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  server.bind((host, port))
  return server

def rodando(server):
  data,address = server.recvfrom(1024)
  data = p.loads(data)
  return data
'''
def func_ping(server,msg,port=5680):
  server.sendto(msg,('<broadcast>',port))


dispositivos = []
servidor = config_serve()
worker1 = Descoberta(servidor,dispositivos)
worker1.start()
msg = p.dumps("aquario1")
'''

# 1.Listar Dispositivos conectados
# 2.Listar funções de um dispositivo especifico
##2.1 (nome dispositivo)
#3.Receber algum dado dos dispositivos
##3.1 (nome dispositivo,função)


dispositivos = []
servidor = config_serve()
servidor2 = config_serve()
servidor_thread = Descoberta(servidor2,dispositivos)
servidor_thread.start()

print("Iniciando Servidor...")
print("Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados")
while True:
  print("Opções = 4")
  comando = input("Digite a opção:")
  try:
    if comando == '1':
      print(f"Dispositivos:{dispositivos}")
      servidor_thread.release()
    
    elif comando == '2':
      msg = [input("Digite o nome do disp:"),'list']
      servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
      print(rodando(servidor))
    elif comando == '3':
      msg = [input("Digite o nome do disp:"),input("Digite a função:")]
      servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
      print(rodando(servidor))
    elif comando == '4':
      print("Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados")
    
  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Finalizando servidor...")
    break
  break


#if __name__=="__main__":
#  main()

#servidor.sendto(msg, ('<broadcast>', 5680))


#func_rec_ping(servidor,dispositivos)
#print(dispositivos)

#while True:
#  data,address = servidor.recvfrom(1024)
#  if not data:
#    break 
#  else:
#    print(p.loads(data))
#print("cabo")

