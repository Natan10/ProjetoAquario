import pika
import uuid
import pickle as p 
import time
import sys

sys.path.append('./Classes')
import request_pb2

class Consume(object):
	def __init__(self):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

		self.channel = self.connection.channel()
    
		result = self.channel.queue_declare(queue='', exclusive=True)
		self.callback_queue = result.method.queue
		
		self.channel.basic_consume(
				queue=self.callback_queue,
				on_message_callback=self.on_response,
				auto_ack=True)

	def on_response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

	def call(self, n):
		self.response = None
		self.corr_id = str(uuid.uuid4())
		self.channel.basic_publish(
				exchange='',
				routing_key='rpc_queue',
				properties=pika.BasicProperties(
						reply_to=self.callback_queue,
						correlation_id=self.corr_id,
				),
				body=str(n))
		while self.response is None:
			print("Esperando dados...")
			self.connection.process_data_events(time_limit=1)
		return self.response


request = request_pb2.Request()
response = request_pb2.Response()

print("Iniciando aplicação...\n")
#print("Quais dispositivos deseja receber dados?")
#print("1: lampada\n2: aquario\n3: portão")
#dispositivos = str(input("Digite as opções?").strip().split(' '))
opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:close"
print(opcoes)
consume = Consume()

while True:
	try:
		comando  = input("Digite a opção:")
		if comando == '1':
			msg = ['1','1']
			response = consume.call(msg)
			time.sleep(0.2)
			print(f"Resposta:{type(response.decode())}")
			print(f"Resposta:{response[0]}")
			
		elif comando == '2':
			nome_do_disp = input("Digite o nome do dispositivo:")
			msg = ['2','2',nome_do_disp]
			response = consume.call(p.dumps(msg))
			time.sleep(0.2)
			print(f"Resposta:{response}")
		
		elif comando == '3':
			nome_do_disp = input("Digite o nome do dispositivo:")
			numero_funcao = input("Digite o numero da funçao:")
			valor = int(input("Digite o valor:"))
			msg = ['3','2',nome_do_disp,numero_funcao,valor]
			response = consume.call(p.dumps(msg))
			time.sleep(0.2)
			print(f"Resposta:{response}")
		
		elif comando == '4':
			msg = ['4','1']
			response = consume.call(p.dumps(msg))
			time.sleep(0.2)
			print(f"Resposta:{response}")

		elif comando == '5':
			msg = ['close']
			response = consume.call(p.dumps(msg))
			time.sleep(0.2)
			print(f"Resposta:{response}")
			break
		else:
			print("Opção não encontrada!")
	except KeyboardInterrupt as e:
		print(e)
		consume.connection.close()
		sys.exit()


