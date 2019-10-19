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




request = request_pb2.Request()
response = request_pb2.Response()

data = []
buffer = []
dispositivos = []
app = config_client()
servidor = config_serve()
servidor_thread = Descoberta(servidor,dispositivos,buffer,data)
servidor_thread.start()

opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:opçoes"
print("Iniciando Servidor...")

while True:
  try:
    print("Esperando conexões...")
    conn,addr = app.accept()
    print("Conectado com",addr)
    
    while True:
      print("Esperando dados...")
      dados = conn.recv(1024)
      request.ParseFromString(dados[:-1])
      if request.comando == 'close':
        break
      print(request)
      buffer.clear()

    # if data:
    #   print(f"Dados Aquario: {data}")
    #   data.clear()
      print("====================================")
      try:
        if request.comando == '1':
          print(f"Dispositivos:{dispositivos}")
          if not dispositivos:
            conteudo = 'nenhum dispositivo na rede'
            response.conteudo = conteudo
          response.conteudo = f'{dispositivos}'
          response.tipo_da_msg = '1'
          conn.send(response.SerializeToString())

        elif request.comando == '2':
          msg = [request.tipo_da_msg,request.nome_do_disp,'list']
          servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
          time.sleep(0.5)
          print(buffer)
          response.tipo_da_msg = '2'
          response.conteudo = f'{buffer[0]}'
          conn.send(response.SerializeToString())
          
        elif request.comando == '3':
          msg = [request.tipo_da_msg,request.nome_do_disp,request.nome_da_func,request.valor]
          servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
          time.sleep(0.5)
          print(buffer)
          response.tipo_da_msg = '2'
          response.conteudo = f'{buffer[0]}'
          conn.send(response.SerializeToString())
        
        elif request.comando == '4':
          msg = [request.tipo_da_msg,"ping"]
          servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
        
      except OSError as msg:
        print(msg)
      except KeyboardInterrupt:
        print("Finalizando servidor...")
        break
  except OSError as e:
    print(e)
  


#request
#    ['comando = 1','tipodamsg = 1'] 
#    ['comando = 2','tipodamsg = 2','list','nomedisp']
#    ['comando = 3','tipodamsg = 2','nomedisp','nomefunc','valor']
#    ['comando = 4','tipodamsg = 1']

#response
#...['tipo','conteudo']