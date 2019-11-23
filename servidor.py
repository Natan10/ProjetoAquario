import sys
import socket
import threading
import time
import pickle as p 
import pika


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
servidor = config_serve()
servidor_thread = Descoberta(servidor,dispositivos,buffer,data)
servidor_thread.start()

print("Iniciando Servidor...")


def processa_requisicao(msg):
  msg = p.loads(msg)    
  try:
    buffer.clear()
    if msg[0] == 'close':
      return 'close'
    
    elif msg[0] == '1':
      print(f"Dispositivos:{dispositivos}")
      if not dispositivos:
        response  = ['1',"nenhum dispositivo na rede"]
      else:
        response = ['1',f"{dispositivos}"]
      return p.dumps(response)
      
    elif msg[0] == '2':
      msg_aux = [msg[1],msg[2],'list']
      if m[2] not in dispositivos:
        response = ['2',"dispositivo inexistente"]
        buffer.clear()
        return p.dumps(response)
      else:  
        servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
        time.sleep(0.5)
        print(buffer)
        response = ['2',f'{buffer[0]}']
        buffer.clear()
        return p.dumps(response)

    elif msg[0] == '3':
      msg_aux = ['2',msg[2],msg[3],msg[4]]
      if msg[2] not in dispositivos:
        response = ['2',f"['dispositivo inexistente']"]
        buffer.clear()
        return p.dumps(response)
      else:
        servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
        time.sleep(0.5)
        print(buffer)
        response = ['2',f"{buffer[0]}"]
        buffer.clear()
        return p.dumps(response)
    
    elif msg[0] == '4':
      msg = ["1","ping"]
      servidor.sendto(p.dumps(msg), ('<broadcast>', 5680))
      time.sleep(0.2)
      response = ['1',f"{dispositivos}"]
      return p.dumps(response)

  except OSError as msg:
    print(msg)
  except KeyboardInterrupt:
    print("Finalizando servidor...")   
    sys.exit()





def main():
  print("Esperando requisições...")
    
  connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

  channel = connection.channel()

  channel.queue_declare(queue='rpc_queue')


  def on_request(ch, method, props, body):
    msg = body
    print(f'Msg_Type:{type(msg.decode())}')
    print(f'Msg:{msg.decode()}')
    #response = processa_requisicao(msg.decode())
    ch.basic_publish(exchange='',
                    routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id = \
                                                        props.correlation_id),
                    body=msg)
    ch.basic_ack(delivery_tag=method.delivery_tag)

  channel.basic_qos(prefetch_count=1)
  channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

  
  channel.start_consuming()


#request
#    ['comando = 1','tipodamsg = 1'] 
#    ['comando = 2','tipodamsg = 2','list','nomedisp']
#    ['comando = 3','tipodamsg = 2','nomedisp','nomefunc','valor']
#    ['comando = 4','tipodamsg = 1']

#response
#...['tipo','conteudo']

if __name__ == '__main__':
  main()