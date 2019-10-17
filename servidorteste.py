import sys
import socket
import threading
import time
import pickle as p 


sys.path.append('./Classes')
from descoberta import Descoberta
import request_pb2

host = ""
port = 5000

def config_serve(host="",port=5000):
  server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  server.bind((host, port))
  return server

def config_client(host="",port=5205):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((host,port))
  server.listen(1)
  return server

teste = request_pb2.Request()
server = config_client()
conn, addr = server.accept()
with conn:
  print('Connected by', addr)
  while True:
    data = conn.recv(1024)
    print(teste.ParseFromString(data))
    
'''

data = []
buffer = []
dispositivos = []
servidor = config_serve()
servidor_thread = Descoberta(servidor,dispositivos,buffer,data)
servidor_thread.start()
opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:opçoes"
print("Iniciando Servidor...")

#request
#    ['comando = 1','tipodamsg = 1'] 
#    ['comando = 2','tipodamsg = 2','list','nomedisp']
#    ['comando = 3','tipodamsg = 2','nomedisp','nomefunc','valor']
#    ['comando = 4','tipodamsg = 1']

#response
#...['tipo','conteudo']

'''
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
  


#if __name__== "__main__":
#  main()

