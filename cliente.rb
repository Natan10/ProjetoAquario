require 'socket'
require_relative 'Classes/request_pb'

cliente = Socket.new Socket::AF_INET, Socket::SOCK_STREAM
cliente.connect Socket.pack_sockaddr_in(5205, '')

puts '*************************'
opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:opçoes\n6:close"
puts opcoes
puts '*************************'

loop {
  puts 'Digite um comando:'
  comando = gets.chomp
  if comando == '1'
    msg = Distribuidos::Request.new(comando:'1',tipo_da_msg:'1')
    cliente.puts Distribuidos::Request.encode(msg)
    resp = cliente.recvfrom(1048)
    puts resp[0]
  
  elsif comando == '2'
    msg = Distribuidos::Request.new(comando:'2',tipo_da_msg:'2',nome_do_disp:gets.chomp)
    cliente.puts Distribuidos::Request.encode(msg)
    resp = cliente.recvfrom(1048)
    puts resp[0]
  
  elsif comando == '3'
    msg = Distribuidos::Request.new(comando:'3',tipo_da_msg:'2',nome_do_disp:gets.chomp,nome_da_func:gets.chomp,valor:gets.to_i)
    cliente.puts Distribuidos::Request.encode(msg)
    resp = cliente.recvfrom(1048)
    puts resp[0]
  
  elsif comando == '4'
    msg = Distribuidos::Request.new(comando:'4',tipo_da_msg:'1')
    cliente.puts Distribuidos::Request.encode(msg)

  elsif comando == '5'
    puts opcoes  

  elsif comando == '6'
    msg = Distribuidos::Request.new(comando:'close')
    cliente.puts Distribuidos::Request.encode(msg)
    cliente.close
    break
  end

}