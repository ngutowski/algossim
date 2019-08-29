#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:16:42 2019

@author: gutowski
"""


import numpy as np
import random

class LinUCB:
    def __init__(self,delta,horizon,d,nbClasses,arms,contexts,ratings):
        self.arms=arms
        self.contexts=contexts
        self.ratings=ratings
        self.setDeltaAlpha(delta)
        self.horizon=horizon
        self.d=d
        self.nbClasses=nbClasses
        self.count=0
        self.Aa=np.zeros((nbClasses,d,d))
        self.ba=np.zeros((nbClasses,d,1))        

        #Not  necessera for LinUCB policy but usefull for knowing the number of selection of each class        
        self.selecteda=np.zeros(nbClasses)

        #Not necessar for LinUCB policy but usefull for observing each features density of theta        
        self.featuresValue={}
        
        for classeId in range (0, nbClasses):
            self.Aa[classeId] = np.identity(self.d)
            self.ba[classeId] = np.zeros((self.d,1)).astype(float)            
            self.selecteda[classeId] = 0
            self.featuresValue[classeId]=[[]]
                 
    def setDeltaAlpha(self, delta):
        if(delta==0):
            self.delta=0
            self.alpha=0
        else:
            self.delta = delta;
            self.alpha = 1 + np.sqrt((np.log(2/delta))/2);
    
    def getAlpha(self):
        return self.alpha
         
    def getDelta(self):
        return self.delta
         
         
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
        

    def getSelecteda(self,classeId):
        return self.selecteda[classeId]         
    
    def setSelecteda(self,classeId):
        self.selecteda[classeId]+=1
    
    def getFeaturesValue(self,classeId):
        return self.featuresValue[classeId]

        
    def chooseAction(self,idCtx):    
        idCls=-1         
        bestPta=-1.0
             
        x=self.getX(idCtx)
                    
             
            
        for i in range (0, self.getNbClasses()):
            if (self.count<self.getNbClasses()):  
                    
                idCls=self.count
                    
                self.count+=1
                    
                    
                break
            else:
                ainv=np.linalg.inv(self.Aa[i])                
                theta=np.dot(ainv, self.ba[i])
                #print(i)
                #print(theta.T)               
                
                
                rewardExpectancy=np.dot(theta.T, x)
                #print(rewardExpectancy)
                
                rewardDeviation=self.getAlpha() * np.sqrt(np.dot(x.T, ainv.dot(x)))
                pta=rewardExpectancy + rewardDeviation
                    
               # print(str(i)+" - pta: "+str(pta)+" - E: "+str(rewardExpectancy)+" - bonus: "+str(rewardDeviation))
                if (pta>bestPta):
                    bestPta=pta                    
                    idCls=i                                       
                elif (pta==bestPta):
                    idCls=random.randint(0,self.getNbClasses()-1)        
               
        
        return idCls
         
    
         
            
    def updateReward(self,idCtx,idCls,evaluation):        
        x=self.getX(idCtx)  
        #print(x.T)
        self.Aa[idCls] = self.Aa[idCls] + np.outer(x,x)
        self.ba[idCls] = self.ba[idCls] + np.multiply(evaluation, x)
        
        ainv=np.linalg.inv(self.Aa[idCls])                
        theta=np.dot(ainv, self.ba[idCls])          
        
        
        #Not necessar for LinUCB policy but usefull for observing each features density of theta        
        self.featuresValue[idCls].append(theta)            
        #Not necessar for LinUCB policy but usefull for observing each features density of theta        
        self.setSelecteda(idCls)
            
     
                        
    def getX(self,idCtx):
             
        return np.array(self.contexts[idCtx].getContextFeat()).reshape(self.getD(),1)
         
            