#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:04:19 2019

@author: gutowski
"""

import random
import numpy as np

class Random:
    def __init__(self,horizon,nbClasses,arms,contexts,ratings):
        self.arms=arms
        self.contexts=contexts
        self.ratings=ratings
        self.horizon=horizon
        self.nbClasses=nbClasses
             
             
            
    def getNbClasses(self):
        return self.nbClasses
            
    def chooseAction(self,idCtx):    
        idCls=random.randint(0,self.getNbClasses()-1)
        
        return idCls
         
    
         
            
    def updateReward(self,idCtx,idCls,evaluation):        
        pass
     
                        
    def getX(self,idCtx):
             
        return np.array(self.contexts[idCtx].getContextFeat()).reshape(self.getD(),1)