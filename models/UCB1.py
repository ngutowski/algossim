#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:51:53 2019

@author: gutowski
"""

import numpy as np
import random


class Ucb1:       

    def __init__(self,horizon,nbClasses,arms,contexts,ratings):
         self.arms=arms
         self.contexts=contexts
         self.ratings=ratings
         self.horizon=horizon
         self.nbClasses=nbClasses
         self.mu_a=np.zeros(nbClasses)
         self.cumulRewarda=np.zeros(nbClasses)
         self.selecteda=np.zeros(nbClasses)
         self.count=0
         self.round=0
         
         for classeId in range (0, nbClasses):
             self.mu_a[classeId] = 1
             self.cumulRewarda[classeId] = 0
             self.selecteda[classeId] = 0    
             
         
    def getRound(self):
        return self.round
     
    def getHorizon(self):
        return self.horizon
     
    def getNbClasses(self):
        return self.nbClasses
        
     
    def getMua(self,classeId):
        return self.mu_a[classeId]
     
    def setMua(self,classeId):
         self.mu_a[classeId]=self.getCumulRewarda(classeId)/self.getSelecteda(classeId)
        
    def getCumulRewarda(self,classeId):
        return self.cumulRewarda[classeId]
    def getSelecteda(self,classeId):
        return self.selecteda[classeId]
    
    def setCumulRewarda(self,classeId,evaluation):
         self.cumulRewarda[classeId]+=evaluation
    def setSelecteda(self,classeId):
         self.selecteda[classeId]+=1
         
        
    def getArms(self):
        return self.arms
     
    def getContexts(self):
        return self.contexts
     
    def getRatings(self):
        return self.ratings
        
        
        
    def chooseAction(self,idCtx):    
         idCls=-1         
         best=-1.0
                     
         self.round+=1
         for i in range (0, self.getNbClasses()):
             if (self.count<self.getNbClasses()):  
                
                idCls=self.count
                
                self.count+=1
                
                
                break
             else:
                   #print(self.getMua(i))
                   esp=self.getMua(i)+2*np.log(self.getRound())/self.getSelecteda(i)
                   if (esp>best):
                           best=esp                     
                           idCls=i                     
                   
         return idCls
      

 
    
    def updateReward(self,idCtx,idCls,evaluation):
         if(evaluation>=1):
             self.setCumulRewarda(idCls,evaluation)
         self.setSelecteda(idCls) 
         self.setMua(idCls)
     
    