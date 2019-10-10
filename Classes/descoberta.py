import socket
import threading
import pickle as p 
import time


class Descoberta(threading.Thread):
  def __init__(self,server,dispositivos,buffer):
    threading.Thread.__init__(self)
    self.server = server
    self.dispositivos = dispositivos
    self.buffer = buffer
  
  def run(self):
    while True:
      try:
        data,address = self.server.recvfrom(1024)
        data = p.loads(data)
        if data[0] == '1':
          if data[1] not in self.dispositivos:
            self.dispositivos.append(data[1])
          elif not data:
            break
        elif data[0] == '2':
          self.buffer.append(data) 

      except OSError as msg:
        print(f"Error:{msg}")
      except KeyboardInterrupt:
        print("Finalizando thread...")
        break