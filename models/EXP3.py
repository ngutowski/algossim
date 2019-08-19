#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:52:50 2019

@author: gutowski
"""

import numpy as np
import random
import math

class Exp3:       

    def __init__(self,gamma,horizon,nbClasses,arms,contexts,ratings):
         self.arms=arms
         self.contexts=contexts
         self.ratings=ratings
         self.horizon=horizon
         self.nbClasses=nbClasses
         self.weights=np.zeros(nbClasses)
         self.probabilities=np.zeros(nbClasses)
         self.gamma=gamma
         self.count=0
         
         for classeId in range (0, nbClasses):
             self.weights[classeId] = 1.0
             self.probabilities[classeId] = 1.0/nbClasses    
         
     
    def getGamma(self):
        return self.gamma
     
    def getHorizon(self):
        return self.horizon
     
    def getNbClasses(self):
        return self.nbClasses
        
     
    def getWeights(self,classeId):
        return self.weights[classeId]
     
        
    def getProbabilities(self,classeId):
        return self.probabilities[classeId]
    
        
    def getArms(self):
        return self.arms
     
    def getContexts(self):
        return self.contexts
     
    def getRatings(self):
        return self.ratings
        
        
        
    def chooseAction(self,idCtx):    
         idCls=-1         
         choice=float(random.randint(0,99))/100                   
         for i in range (0, self.getNbClasses()):
             sum=0
             if (self.count<self.getNbClasses()):                
                idCls=self.count                
                self.count+=1                
                break
             else:                 
                 for i in range (0,self.getNbClasses()):
                     sum += self.getProbabilities(i)
                     if (choice <= sum):
                         idCls = i
                         break
         #print(str(choice)+"-"+str(sum))
         return idCls      

 
    
    def updateReward(self,idCtx,idCls,evaluation):
         estimatedReward = evaluation / self.getProbabilities(idCls);
         self.weights[idCls]= self.weights[idCls]*math.exp(estimatedReward*self.getGamma()/self.nbClasses)
         sum=0
         for i in range (0,self.getNbClasses()):
             sum+=self.getWeights(i)
         
         for i in range (0,self.getNbClasses()):
             self.probabilities[i]= (1 - self.getGamma())*self.getWeights(i)/sum+self.getGamma()/self.nbClasses