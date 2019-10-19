import socket 

#UDP
def config_sensor(host,port):
  meia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  meia.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  meia.bind((host,port))
  return meia

#UDP
def config_serve(host="",port=5000):
  server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  server.bind((host, port))
  return server

#TCP
def config_cliente(host="",port=5205):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((host,port))
  server.listen(1)
  return server