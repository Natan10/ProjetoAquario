#Classe Portao
# Nome_Luz :
# Ligada: Ligada / Desligada
# Ativar: Liga / Desliga a Luz
# Potencia: Ajusta a potência da luz, se possível... Como fazer um método opcional? acho melhor não fazer kkk

import random
import time 

class luz:
  def __init__(self,nome, ligada = False):
    self.nome = nome
    self.ligada = ligada
  
  def get_nome(self):
    return self.nome 

  def get_estado_luz(self):
    if self.ligada == True:
      return "Ligada" 
    else:
      return "Desliga"
  
  def set_ativar(self):
    if self.ligada == True:
      #função para fechar o portao
      self.ligada = False:
      return "A luz foi ligada" 
    else:
      self.ligada = True:
      return "A luz foi desliga"