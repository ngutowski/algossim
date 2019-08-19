#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:53:05 2019

@author: gutowski
"""

import numpy as np
import random
import math

class LinearThompsonSampling:       

    def __init__(self,r,delta,horizon,d,nbClasses,arms,contexts,ratings):
         self.arms=arms
         self.contexts=contexts
         self.ratings=ratings
         self.horizon=horizon
         self.d=d
         self.nbClasses=nbClasses
         self.count=0
         self.Ba=np.zeros((nbClasses,d,d))
         self.fa=np.zeros((nbClasses,d,1))
         self.v2 = math.pow(r*math.sqrt(9*d*math.log(horizon/delta)),2)
         
         for classeId in range (0, nbClasses):
             self.Ba[classeId] = np.identity(self.d)
             self.fa[classeId] = np.zeros((self.d,1)).astype(float)
          
                 
      
    def getV2(self):
        return self.v2
     
     
     
    def getHorizon(self):
        return self.horizon
     
    def getNbClasses(self):
        return self.nbClasses
        
    def getD(self):
        return self.d
     
    def getb(self,classeId):
        return self.ba[classeId]
        
    def getA(self,classeId):
        return self.Aa[classeId]
     
    def getA_inv(self,classeId):
        return self.Aa_inv[classeId]
        
    def getArms(self):
        return self.arms
     
    def getContexts(self):
        return self.contexts
     
    def getRatings(self):
        return self.ratings
        
        
        
    def chooseAction(self,idCtx):    
         idCls=-1         
         best=-1.0
         
         x=self.getX(idCtx)
                
         
        
         for i in range (0, self.getNbClasses()):
             if (self.count<self.getNbClasses()):  
                
                idCls=self.count
                
                self.count+=1
                
                
                break
             else:
                binv=np.linalg.inv(self.Ba[i])
                binvV2=np.multiply(binv,self.getV2())
                mu=np.ndarray.flatten(np.dot(binv, self.fa[i]))
                sample=np.random.multivariate_normal(mu,binvV2)
                rwExp=np.absolute(np.dot(sample.T, x))
                
                                
                
                
                #print(str(i)+" - rwExp: "+str(rwExp))
                if (rwExp>best):
                     best=rwExp                    
                     idCls=i                     
                elif (rwExp==best):
                     idCls=random.randint(0,self.getNbClasses()-1)
    
         return idCls

 
    
    def updateReward(self,idCtx,idCls,evaluation):        
        x=self.getX(idCtx)        
        self.Ba[idCls] = self.Ba[idCls] + np.outer(x,x)
        self.fa[idCls] = self.fa[idCls] + np.multiply(evaluation, x)
    
 
                
    def getX(self,idCtx):
         
        return np.array(self.contexts[idCtx].getContextFeat()).reshape(self.getD(),1)         
     
