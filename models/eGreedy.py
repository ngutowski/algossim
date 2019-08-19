#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:42:01 2019

@author: gutowski
"""

import numpy as np
import random

class eGreedy:       
        
    def __init__(self,epsilon,horizon,nbClasses,arms,contexts,ratings):
        self.arms=arms
        self.contexts=contexts
        self.ratings=ratings
        self.setEpsilon(epsilon)
        self.horizon=horizon
        self.nbClasses=nbClasses
        self.mu_a=np.zeros(nbClasses)
        self.cumulRewarda=np.zeros(nbClasses)
        self.selecteda=np.zeros(nbClasses)
        self.count=0
         
        for classeId in range (0, nbClasses):
            self.mu_a[classeId] = 1
            self.cumulRewarda[classeId] = 0
            self.selecteda[classeId] = 0    
             
         
    def setEpsilon(self, epsilon):
        self.epsilon=epsilon

     
     
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
        
    def getEpsilon(self):
        return self.epsilon
        
        
    def chooseAction(self,idCtx):    
         idCls=-1         
         bestMua=-1.0
                     
        
         for i in range (0, self.getNbClasses()):
             if (self.count<self.getNbClasses()):  
                
                idCls=self.count
                
                self.count+=1
                
                
                break
             else:
                   adv=random.randint(0,100)
                   
                   if(self.getEpsilon()*100<adv):
                       if (self.getMua(i) >bestMua):
                           bestMua=self.getMua(i)                     
                           idCls=i                     
                  
         return idCls
          
    
     
        
    def updateReward(self,idCtx,idCls,evaluation):
         if(evaluation>=1):
             self.setCumulRewarda(idCls,evaluation)
         self.setSelecteda(idCls)
         self.setMua(idCls)
     
