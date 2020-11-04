# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:14:24 2019

@author: raghed
"""
class Monnaie(object):
  valeur=0
  devise ='LL'
    
  def __init__(self, devise):
      self.devise = devise
  
 
  def ajouter(self,val):
      self.valeur += val
      
  
  def retrancher(self,val):
      self.valeur -= val

  def rendreMonnaieIterative(self,typeBillet,val):
      change={}
      for x in typeBillet:
          change[x]=val//x
          val%=x
      print(change)
      
      

      

m1 = Monnaie("LL")
m2 = Monnaie("EUR")

types=(5000,1000)
m1.rendreMonnaieIterative(types,7000)
