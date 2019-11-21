import pika
import pickle as p


class Server():
  def __init__(self):
    self.connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    self.channel = self.connection.channel()
    result = self.channel.queue_declare(queue='rpc_queue')
    self.channel.basic_consume(
        queue='rpc_queue',
        on_message_callback=self.on_request)

#  def __init__(self):
#    self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#    self.channel = self.connection.channel()
#    self.channel.queue_declare(queue='rpc_queue')
#    self.channel.basic_consume(queue='rpc_queue', on_message_callback= on_request)


  def on_request(ch, method, props, body):
    msg = str(body)
    response = msg
    self.ch.basic_publish(exchange='',routing_key=props.reply_to,properties=pika.BasicProperties(correlation_id = props.correlation_id),body=str(response))
    self.ch.basic_ack(delivery_tag=method.delivery_tag) 
  