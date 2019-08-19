#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:11:08 2019

@author: gutowski
"""
from models.Random import Random
from models.LinUCB import LinUCB
from models.eGreedy import eGreedy
from models.EXP3 import Exp3
from models.UCB1 import Ucb1
from models.ThompsonSampling import ThompsonSampling
from models.LinTS import LinearThompsonSampling

class Model:              
    
    
    def __init__(self,algorithm,horizon,d,nbClasses,arms,contexts,ratings):
        
        if(algorithm=="random"):
            self.algo=Random(horizon,nbClasses,arms,contexts,ratings)      
          
        elif(algorithm=="linucb"):      
            self.algo=LinUCB(0.1,horizon,d,nbClasses,arms,contexts,ratings)
            
        elif(algorithm=="egreedy"):
            self.algo=eGreedy(0.1,horizon,nbClasses,arms,contexts,ratings)
        
        elif(algorithm=="ucb1"):
            self.algo=Ucb1(horizon,nbClasses,arms,contexts,ratings)
        elif(algorithm=="ts"):
            self.algo=ThompsonSampling(horizon,nbClasses,arms,contexts,ratings)

        elif(algorithm=="lints"):
            self.algo=LinearThompsonSampling(0.01,0.1,horizon,d,nbClasses,arms,contexts,ratings)
        
        elif(algorithm=="exp3"):
            self.algo=Exp3(0.1,horizon,nbClasses,arms,contexts,ratings)      
            
       
        self.ratings=ratings
        self.horizon=horizon
    
    
    def evaluate(self,idCtx,idCls):
        evaluation=self.ratings[str(idCtx),str(idCls)]
        return evaluation
    
    def getAlgo(self):
        return self.algo
    
    
    
 
                   
    
    

            
            

		