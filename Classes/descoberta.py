import socket
import threading
import pickle as p 
import time


class Descoberta(threading.Thread):
  def __init__(self,server,dispositivos):
    threading.Thread.__init__(self)
    self.server = server
    self.dispositivos = dispositivos
  
  def run(self):
    print("Iniciando thread...")
    while True:
      try:
        data,address = self.server.recvfrom(1024)
        data = p.loads(data)
        if data not in self.dispositivos:
          self.dispositivos.append(data)
        elif not data:
          break
      except OSError as msg:
        print(f"Error:{msg}")
      except KeyboardInterrupt:
        print("Finalizando thread...")
        break