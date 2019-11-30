# frozen_string_literal: true

require 'bunny'
require_relative 'Classes/request_pb'

class Consume
  attr_accessor :call_id, :response, :lock, :condition, :connection,
                :channel, :server_queue_name, :reply_queue, :exchange

  def initialize(server_queue_name)
    @connection = Bunny.new(automatically_recover: false)
    @connection.start

    @channel = connection.create_channel
    @exchange = channel.default_exchange
    @server_queue_name = server_queue_name

    setup_reply_queue
  end

  def call(n)
    @call_id = generate_uuid

    exchange.publish(n.to_s,
                     routing_key: server_queue_name,
                     correlation_id: call_id,
                     reply_to: reply_queue.name)

    # wait for the signal to continue the execution
    lock.synchronize { condition.wait(lock) }

    response
  end

  def stop
    channel.close
    connection.close
  end

  private

  def setup_reply_queue
    @lock = Mutex.new
    @condition = ConditionVariable.new
    that = self
    @reply_queue = channel.queue('', exclusive: true)

    reply_queue.subscribe do |_delivery_info, properties, payload|
      if properties[:correlation_id] == that.call_id
        that.response = payload.to_i

        # sends the signal to continue the execution of #call
        that.lock.synchronize { that.condition.signal }
      end
    end
  end

  def generate_uuid
    # very naive but good enough for code examples
    rand.to_s
  end
end

def assinar_disp(dispositivos, escolha)
  escolha.clear
  puts("Para fechar digite 's' ou 'sair'")
  loop do
    d = input('assinar dispositivo:').lower
    if %w[s sair].include?(d)
      break
    elsif !dispositivos.include?(d)
      puts('dispositivo inexistente!')
    else
      escolha << d unless escolha.include?(d)
    end
  end
end

client = Consume.new('rpc_queue')

dispositivos = %w[lamp aq port]
escolha = []
puts("Iniciando aplicação...\n")
puts('Quais dispositivos deseja receber dados?')
puts("Lampada:lamp\nAquario:aq\nPortao:port\n")


assinar_disp(dispositivos,escolha)

opcoes = "Opções:\n1:Listar Dispositivos conectados\n2:Listar funçoes\n3:Receber dados\n4:descobrir dispositivos\n5:assinaturas\n6:muda ass\n7:menu\n8:close"

puts '===' * 10
puts opcoes
puts '===' * 10

loop do
  begin
    p "Digite a opção [7:menu] :"
    comando = gets.chomp

  if comando == '1'
    msg = Distribuidos::Request.new(comando: '1', tipo_da_msg: '1')
    response = client.call(msg)
    puts "Resposta : #{Distribuidos::Request.encode(response)}"

  elsif comando == '2'
    puts 'Digite o nome do dispositivo:'
    nome_do_disp = gets.chomp
    msg = Distribuidos::Request.new(comando: '2', tipo_da_msg: '2', nome_do_disp: nome_do_disp)
    response = client.call(msg)
    puts "Resposta : #{Distribuidos::Request.encode(response)}"
    

  elsif comando == '3'
    puts 'Digite o nome do dispositivo:'
    nome_do_disp = gets.chomp
    puts 'Digite o numero da funçao:'
    nome_da_func =  gets.chomp
    puts 'Digite um valor se a funçao for set:'
    valor = gets.to_i
    msg = Distribuidos::Request.new(comando: '3', tipo_da_msg: '2', nome_do_disp: nome_do_disp, nome_da_func: nome_da_func, valor: valor)
    response = client.call(msg)
    puts "Resposta : #{Distribuidos::Request.encode(response)}"

  elsif comando == '4'
    msg = Distribuidos::Request.new(comando: '4', tipo_da_msg: '1')
    response = client.call(msg)
    puts "Resposta : #{Distribuidos::Request.encode(response)}"

  elsif comando == '5'
    puts "Assinaturas:#{escolha}"

  elsif comando == '6'
    assinar_disp(dispositivos,escolha)
  
  elsif comando == '7'
    puts opcoes

  elsif comando == '8'
    msg = Distribuidos::Request.new(comando: 'close')
    response = client.call(msg)
    puts "Resposta : #{Distribuidos::Request.encode(response)}"
    cliente.close
    break
  end

  rescue Interrupt => _
    client.stop
    break
  end
end


