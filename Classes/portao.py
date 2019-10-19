#Classe Portao
# Nome_Portao :
# Aberto: Aberto = 1 / Fechado = 0
# Ativar: Abre / Fecha o Portao
# Lembrar: Se o Portao ficar mais de dois minutos aberto, manda um aviso

import random
import time 

class Portao:
  def __init__(self,nome, aberto = 1):
    self.nome = nome
    self.aberto = aberto

  def get_nome(self):
    return self.nome 

  def get_estado_portao(self):
    return aberto

  def set_estado_portao(self):
    if self.aberto == 1:
      self.aberto = 0
      return "Portao fechado!"
    else:
      self.aberto = 1
      return "Portao aberto!"

 
