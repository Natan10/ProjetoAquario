#Classe Portao
# Nome_Portao :
# Aberto: Aberto = 1 / Fechado = 0
# Ativar: Abre / Fecha o Portao
# Lembrar: Se o Portao ficar mais de dois minutos aberto, manda um aviso

import random
import time 

class Portao:
  def __init__(self,nome, aberto = 0, lembrete = 0, tempo = 0):
    self.nome = nome
    self.aberto = aberto
    self.tempo = tempo
  def get_nome(self):
    return self.nome 

  def get_estado_portao(self):
    return self.aberto

  def set_estado_portao(self):
    if self.aberto == 1:
      self.aberto = 0
      self.tempo = 0
      return "Portao fechado!"
    else:
      self.aberto = 1
      self.tempo = time.time()
      return "Portao aberto!"

  def aviso(self):
    if(self.get_estado_portao()):
      if( (time.time() - self.tempo()) > 20):
        return "O portao ainda esta aberto"
      else:
        return 0



 
