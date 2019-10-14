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
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((host, port))
  return server


# 1.Listar Dispositivos conectados
# 2.Listar funções de um dispositivo especifico
##2.1 (nome dispositivo)
#3.Receber algum dado dos dispositivos
##3.1 (nome dispositivo,função)
### Mensagens (msg,tipo)

data = []
buffer = []
dispositivos = [] # lista com os dispositivos já conectados no servidor
servidor = config_serve()
servidor_thread = Descoberta(servidor,dispositivos,buffer,data)
servidor_thread.start()
opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:opçoes"
print("Iniciando Servidor...")

while True:
  buffer.clear()
  print("Op = 5")
  if data:
    print(f"Dados Aquario: {data}")
    data.clear()
  print("====================================")
  comando = input("Digite a opção:")
  try:
    if comando == '1':
      print(f"Dispositivos:{dispositivos}")

    elif comando == '2':
      msg = ['2',input("Digite o nome do disp:"),'list']
      servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
      time.sleep(0.5)
      print(buffer)
      
    elif comando == '3':
      msg = ['2',input("Digite o nome do disp:"),input("Digite o numero da func:"),input("digite o valor:")]
      servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
      time.sleep(0.5)
      print(buffer)
    
    elif comando == '4':
      msg = ['1',"ping"]
      servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
      
    elif comando == '5':
      print(opcoes)
    
  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Finalizando servidor...")
    break
  print("====================================")
  


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

