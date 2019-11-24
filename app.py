import pika
import uuid
import pickle as p 
import time
import sys

sys.path.append('./Classes')
sys.path.append('./Funcoes')
from consume import Consume
from funcoes import *


dispositivos = ['lamp','aq','port']
escolha = []
print("Iniciando aplicação...\n")
print("Quais dispositivos deseja receber dados?")
print("Lampada:lamp\nAquario:aq\nPortao:port\n")


	
assinar_disp(dispositivos,escolha)

opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:assinaturas\n6:muda ass\n7:menu\n8:close"
print(opcoes)
consume = Consume()

while True:
	try:
		comando  = input("Digite a opção [7:menu] :")
		if comando == '1':
			dados = consume.call("1 1")
			time.sleep(0.2)
			print(f"Resposta:{p.loads(dados)}")
			print("\n")

			
		elif comando == '2':
			nome_do_disp = input("Digite o nome do dispositivo:")
			if nome_do_disp in escolha:
				dados = consume.call(f"2 2 {nome_do_disp}")
				dados = p.loads(dados)	
				print(f"Resposta:{dados[0]}")
			else:
				print("Você não possui assinatura desses dispositivo!")
			print("\n")

		
		elif comando == '3':
			nome_do_disp = input("Digite o nome do dispositivo:")
			if nome_do_disp in escolha:
				numero_funcao = input("Digite o numero da funçao:")
				valor = int(input("Digite o valor:"))
				dados = consume.call(f"3 2 {nome_do_disp} {numero_funcao} {valor}")
				dados = p.loads(dados)
				print(f"Resposta:{dados[0]}")
			else:
				print("Você não possui assinatura desses dispositivo!")
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


