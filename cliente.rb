# frozen_string_literal: true

require 'socket'
require_relative 'Classes/request_pb'

cliente = Socket.new Socket::AF_INET, Socket::SOCK_STREAM
cliente.connect Socket.pack_sockaddr_in(5205, '')

x = Distribuidos::Response.new

opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:close"

puts '===' * 10
puts opcoes
puts '===' * 10

loop do
  puts '===' * 10
  puts 'Digite um comando:'
  comando = gets.chomp

  if comando == '1'
    msg = Distribuidos::Request.new(comando: '1', tipo_da_msg: '1')
    cliente.puts Distribuidos::Request.encode(msg)

  elsif comando == '2'
    puts 'Digite o nome do dispositivo:'
    nome_do_disp = gets.chomp
    msg = Distribuidos::Request.new(comando: '2', tipo_da_msg: '2', nome_do_disp: nome_do_disp)
    cliente.puts Distribuidos::Request.encode(msg)

  elsif comando == '3'
    puts 'Digite o nome do dispositivo:'
    nome_do_disp = gets.chomp
    puts 'Digite o numero da funçao:'
    nome_da_func =  gets.chomp
    puts 'Digite um valor se a funçao for set:'
    valor = gets.to_i
    msg = Distribuidos::Request.new(comando: '3', tipo_da_msg: '2', nome_do_disp: nome_do_disp, nome_da_func: nome_da_func, valor: valor)
    cliente.puts Distribuidos::Request.encode(msg)

  elsif comando == '4'
    msg = Distribuidos::Request.new(comando: '4', tipo_da_msg: '1')
    cliente.puts Distribuidos::Request.encode(msg)

  elsif comando == '5'
    msg = Distribuidos::Request.new(comando: 'close')
    cliente.puts Distribuidos::Request.encode(msg)
    cliente.close
    break
  end

  resp = cliente.recvfrom(1024)
  resp = resp[0].to_s
  if resp.match(/data/)
    puts '== Dados do Aquario =='
    puts "Dados do Aquario: #{resp.match(/\[.*\]/)}"
  else
    puts '==Resposta do servidor=='
    puts resp.match(/\[.*\]/)
  end
end
