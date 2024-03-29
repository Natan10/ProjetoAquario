import sys
import socket
import threading
import time
import pickle as p 


sys.path.append('./Classes')
sys.path.append('./Funcoes')
from descoberta import Descoberta
from funcoes import *
import request_pb2

host = ""
port = 5000


request = request_pb2.Request()
response = request_pb2.Response()

data = []
buffer = []
dispositivos = []
app = config_cliente()
servidor = config_serve()
servidor_thread = Descoberta(servidor,dispositivos,buffer,data)
servidor_thread.start()


print("Iniciando Servidor...")

def main():
  while True:
    try:
      print("Esperando conexões...")
      conn,addr = app.accept()
      print("Conectado com",addr)
      
      while True:
        buffer.clear()
        print("Esperando dados...")
        dados = conn.recv(1024)
        request.ParseFromString(dados[:-1])
        if request.comando == 'close':
          break
        print(request)
        
        if data:
          response.tipo_da_msg = 'data'
          response.conteudo = f'{data[0]}'
          conn.send(response.SerializeToString())
          data.clear()

        print("====================================")
        try:
          if request.comando == '1':
            print(f"Dispositivos:{dispositivos}")
            if not dispositivos:
              response.conteudo = f"['nenhum dispositivo na rede']"
            else:
              response.conteudo = f'{dispositivos}'
            response.tipo_da_msg = '1'
            conn.send(response.SerializeToString())

          elif request.comando == '2':
            msg = [request.tipo_da_msg,request.nome_do_disp,'list']
            if request.nome_do_disp not in dispositivos:
              response.tipo_da_msg = '2'
              response.conteudo = f"['dispositivo inexistente']"
              conn.send(response.SerializeToString())
              buffer.clear()
            else:  
              servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
              time.sleep(0.5)
              print(buffer)
              response.tipo_da_msg = '2'
              response.conteudo = f'{buffer[0]}'
              conn.send(response.SerializeToString())
              buffer.clear()
            
          elif request.comando == '3':
            msg = [request.tipo_da_msg,request.nome_do_disp,request.nome_da_func,request.valor]
            if request.nome_do_disp not in dispositivos:
              response.tipo_da_msg = '2'
              response.conteudo = f"['dispositivo inexistente']"
              conn.send(response.SerializeToString())
              buffer.clear()
            else:
              servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
              time.sleep(0.5)
              print(buffer)
              response.tipo_da_msg = '2'
              response.conteudo = f'[{buffer[0]}]'
              conn.send(response.SerializeToString())
              buffer.clear()
          
          elif request.comando == '4':
            msg = [request.tipo_da_msg,"ping"]
            servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
            time.sleep(0.2)
            response.conteudo = f'{dispositivos}'
            response.tipo_da_msg = '1'
            conn.send(response.SerializeToString())

        except OSError as msg:
          print(msg)
        except KeyboardInterrupt:
          print("Finalizando servidor...")   
          sys.exit()
    except OSError as e:
      print(e)
  


#request
#    ['comando = 1','tipodamsg = 1'] 
#    ['comando = 2','tipodamsg = 2','list','nomedisp']
#    ['comando = 3','tipodamsg = 2','nomedisp','nomefunc','valor']
#    ['comando = 4','tipodamsg = 1']

#response
#...['tipo','conteudo']

if __name__ == '__main__':
  main()