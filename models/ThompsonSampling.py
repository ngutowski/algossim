#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:52:14 2019

@author: gutowski
"""

import numpy as np
import random

     
class ThompsonSampling:       

    def __init__(self,horizon,nbClasses,arms,contexts,ratings):
         self.arms=arms
         self.contexts=contexts
         self.ratings=ratings
         self.horizon=horizon
         self.nbClasses=nbClasses
         self.regret=np.zeros(nbClasses)
         self.reward=np.zeros(nbClasses)
         self.count=0
         
         
    def getHorizon(self):
        return self.horizon
     
    def getNbClasses(self):
        return self.nbClasses
        
     
    def getRegret(self,classeId):
        return self.regret[classeId]
     
    def getReward(self,classeId):
        return self.reward[classeId]
     
    def setRegret(self,classeId):
         self.regret[classeId]+=1
     
    def setReward(self,classeId):
         self.reward[classeId]+=1   
     
         
        
    def getArms(self):
        return self.arms
     
    def getContexts(self):
        return self.contexts
     
    def getRatings(self):
        return self.ratings
        
        
        
    def chooseAction(self,idCtx):    
         idCls=-1         
         best=-1.0
                     
         for i in range (0, self.getNbClasses()):
             if (self.count<self.getNbClasses()):  
                
                idCls=self.count
                
                self.count+=1
                
                
                break
             else:
                   sample=np.random.beta(self.reward[i]+1,self.regret[i]+1)
                   if (sample>best):
                           best=sample                     
                           idCls=i                     
                 
         return idCls      

 
    
    def updateReward(self,idCtx,idCls,evaluation):
         if(evaluation>=1):
             self.setReward(idCls)
         else:
             self.setRegret(idCls) 
                  
 

     