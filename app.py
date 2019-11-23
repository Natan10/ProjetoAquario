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
			self.connection.process_data_events(time_limit=2)
		return self.response

dispositivos = ['lamp','aq','port']
escolha = []
print("Iniciando aplicação...\n")
print("Quais dispositivos deseja receber dados?")
print("Lampada:lamp\nAquario:aq\nPortao:port\n")

def assinar_disp(dispositivos,escolha):
	escolha.clear()
	while True:
		d = input("assinar dispositivo:").lower()
		if d in ['s','sair']:
			break
		elif d not in dispositivos:
			print("dispositivo inexistente!")
		else:
			if d not in escolha:
				escolha.append(d)
	
assinar_disp(dispositivos,escolha)

opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:assinaturas\n6:muda ass\n7:menu\n8:close"
print(opcoes)
consume = Consume()

while True:
	try:
		comando  = input("Digite a opção [7:menu] :")
		if comando == '1':
			dados = consume.call("1 1 teste")
			time.sleep(0.2)
			print(f"Resposta:{p.loads(dados)}")
			print("\n")

			
		elif comando == '2':
			nome_do_disp = input("Digite o nome do dispositivo:")
			dados = consume.call(f"2 2 {nome_do_disp}")
			time.sleep(0.2)
			print(f"Resposta:{p.loads(dados)}")
			print("\n")

		
		elif comando == '3':
			nome_do_disp = input("Digite o nome do dispositivo:")
			numero_funcao = input("Digite o numero da funçao:")
			valor = int(input("Digite o valor:"))
			dados = consume.call(f"3 2 {nome_do_disp} {numero_funcao} {valor}")
			time.sleep(0.2)
			print(f"Resposta:{p.loads(dados)}")
			print("\n")

		
		elif comando == '4':
			msg = ['4','1']
			dados = consume.call('4 1')
			time.sleep(0.2)
			print(f"Resposta:{p.loads(dados)}")

		elif comando == '5':
			print(f'Assinatura: {escolha}')
			print("\n")

			
		elif comando == '6':
			assinar_disp(dispositivos,escolha)
			print("\n")

		elif comando == '7':
			print(opcoes)

		elif comando == '8':
			consume.connection.close()
			break
		else:
			print("Opção não encontrada!")
	except KeyboardInterrupt as e:
		print(e)
		consume.connection.close()
		sys.exit()


