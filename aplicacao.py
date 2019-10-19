import socket
import sys
print('A quem deseja se conectar?')
host = input('qual o endereço de host:')
porta = int(input('qual o endereço da porta:'))

	
sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockTCP.connect((host, porta))

data = '1'	

while data :		
	resposta = sockTCP.recv(1024)
	print(resposta.decode("utf-8"))	

	data = input()
	
	if(data == r'\CLOSE'):
		break
	sockTCP.send(bytes(data,'utf-8'))
		
print('Conexão Encerrada')
sockTCP.close()
