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
print("Iniciando aplicação...")
print("\n===========================================================================\n")
print("Selecione os dispositivos dos quais deseja receber dados:")
print("-> Lampada: lamp\n-> Aquario: aq\n-> Portao: port\n-> Encerrar escolha: s\n")
	
assinar_disp(dispositivos, escolha)

opcoes = "Selecione uma das operações abaixo:\n1: Listar Dispositivos conectados\n2: Listar funções\n3: Receber dados\n4: Descobrir dispositivos\n5: Dispositivos selecionados\n6: Mudar seleção de dispositivos\n7: Encerrar aplicação\n"
consume = Consume()

while True:
	try:
		print("\n===========================================================================\n")
		print(opcoes)
		comando  = input("R: ")
		print("\n---------------------------------------------------------------------------\n")

		if comando == '1':
			dados = consume.call("1 1")
			time.sleep(0.2)
			print(f"\nResposta: {p.loads(dados)}")
			print()

		elif comando == '2':
			nome_do_disp = input("Digite o nome do dispositivo: ")
			if nome_do_disp in escolha:
				dados = consume.call(f"2 2 {nome_do_disp}")
				dados = p.loads(dados)	
				print(f"\nResposta: {dados[0]}")
			else:
				print("\nVocê não selecionou esse dispositivo!")
			print()

		elif comando == '3':
			nome_do_disp = input("Digite o nome do dispositivo: ")
			if nome_do_disp in escolha:
				numero_funcao = input("Digite o número da função: ")
				valor = int(input("Digite o valor: "))
				dados = consume.call(f"3 2 {nome_do_disp} {numero_funcao} {valor}")
				dados = p.loads(dados)
				print(f"\nResposta: {dados[0]}")
			else:
				print("\nVocê não selecionou esse dispositivo!")
			print()

		elif comando == '4':
			msg = ['4','1']
			dados = consume.call('4 1')
			time.sleep(0.2)
			print(f"\nResposta: {p.loads(dados)}")

		elif comando == '5':
			print(f'Dispositivos selecionados: {escolha}')
			print()

		elif comando == '6':
			print("Selecione os dispositivos dos quais deseja receber dados:")
			print("-> Lampada: lamp\n-> Aquario: aq\n-> Portao: port\n-> Encerrar escolha: s\n")

			assinar_disp(dispositivos,escolha)
			print()

		elif comando == '7':
			consume.connection.close()
			break
		else:
			print("Opção não é válida!")
			print()

		input("(Aperte ENTER para continuar...)")
	except KeyboardInterrupt as e:
		print(e)
		consume.connection.close()
		sys.exit()