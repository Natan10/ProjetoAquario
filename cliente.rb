require 'socket'
require_relative '/home/natan/Documentos/Natan/UFC/Distribuidos/protoc-3.10.0/bin/request_pb'

cliente = Socket.new Socket::AF_INET, Socket::SOCK_STREAM
cliente.connect Socket.pack_sockaddr_in(5205, '')

puts '*************************'
opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:opçoes"
puts opcoes
puts '*************************'

loop {
  puts 'Digite um comando:'
  comando = gets.chomp
  if comando == '1'
    msg = Distribuidos::Request.new(comando:'1',tipo_da_msg:'1')
    #cliente.puts Distribuidos::Request.encode(msg)
    cliente.puts msg
  elsif comando == '2'
    msg = Distribuidos::Request.new(comando:'2',tipo_da_msg:'2',nome_do_disp:gets.chomp)
    cliente.puts Distribuidos::Request.encode(msg)

  elsif comando == '3'
    msg = Distribuidos::Request.new(comando:'2',tipo_da_msg:'2',nome_do_disp:gets.chomp,nome_da_func:gets.chomp,valor:gets.to_i)
    cliente.puts Distribuidos::Request.encode(msg)

  elsif comando == '4'
    msg = Distribuidos::Request.new(comando:'4',tipo_da_msg:'1')
    cliente.puts Distribuidos::Request.encode(msg)
  
  elsif comando == '5'
    puts opcoes  
  end

  resp = cliente.recvfrom(1024)
  puts resp 
  cliente.close
} 