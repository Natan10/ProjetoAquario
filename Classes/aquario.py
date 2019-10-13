#Classe Aquario
# Nome_Aquario :
# Luz : Ligada / Desligada
# Comida : Quantidade e aviso de falta de comida
# Filtro : Quantidade de O²

import random
import time 

class Aquario:
  def __init__(self,nome,luz = 1,comida = 10):
    self.nome = nome
    self.luz = luz
    self.comida = comida
  
  def get_nome(self):
    return self.nome

  def get_estado_luz(self):
    if self.luz == 1:
      return "Ligada" 
    else:
      return "Desligada"
  
  def set_estado_luz(self,estado):
    self.luz = estado

  def get_qtd_comida(self):
    if self.comida < 10: 
      return "Comida acabando!" 
    else: 
      return self.comida

  def set_estado_comer(self,value):
    if value > self.comida:
      return "Comida insuficiente!"
    else:
      self.comida -= value

  def set_estado_addcomida(self,value):
    self.comida += value

  def get_estado_filtro(self):
    return f"{random.random()*100}% de O2" 
  
  def get_estado_aquario(self):
    return [self.nome,self.luz,self.comida,self.get_estado_filtro()]
