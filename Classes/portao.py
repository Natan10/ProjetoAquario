#Classe Portao
# Nome_Portao :
# Aberto: Aberto / Fechado
# Ativar: Abre / Fecha o Portao
# Lembrar: Se o Portao ficar mais de dois minutos aberto, manda um aviso

import random
import time 

class Portao:
  def __init__(self,nome, aberto = False, lembrar = False):
    self.nome = nome
    self.aberto = aberto
    self.lembrar = lembrar
  
  def get_nome(self):
    return self.nome 

  def get_estado_portao(self):
    if self.aberto == True:
      return "Aberto" 
    else:
      return "Fechado"
 ### 
#  def set_ativar(self):
#    if self.aberto == True:
      #função para fechar o portao
#      self.aberto = False:
#      return "O portão foi aberto" 
#    else:
#      self.aberto = True:
#      return "O portão foi fechado"
###
  def lembrar(self):
    if self.aberto == True: 
      time_start = time.time()
      while(self.aberto) :
        if((time.time() - time_start) > 120):
          return("O Portao está aberto!")