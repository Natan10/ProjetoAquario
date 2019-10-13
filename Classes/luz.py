#Classe Portao
# Nome_Luz :
# Ligada: Ligada / Desligada
# Ativar: Liga / Desliga a Luz
# Potencia: Ajusta a potência da luz, se possível... Como fazer um método opcional? acho melhor não fazer kkk

import random
import time 

class Luz:
  def __init__(self,nome, ligada = 0):
    self.nome = nome
    self.ligada = ligada
  
  def get_nome(self):
    return self.nome 

  def get_estado_luz(self):
    if self.ligada == 1:
      return "Ligada" 
    else:
      return "Desliga"
  
  def set_estado_luz(self):
    if self.ligada == 1:
      self.ligada = 0
      return "Luz desligada!" 
    else:
      self.ligada = 1
      return "Luz ligada!"