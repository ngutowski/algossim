#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:37:44 2019

@author: gutowski
"""

from data.DataMonitor import dataStore
#import LinUCB as lb
import Model as m
import sys
from scipy.stats import variation
import random
import math

from View import viewGraphic,displayRound,displayDataInformations,displayAlgorithmInformations,figure,dynamicView,nameProcessing
#from View import plot3D

def execute(nameDataset=str(sys.argv[1]),nameAlgorithm=str(sys.argv[2]),horizon=int(sys.argv[3])):
    
    storeData=dataStore(nameDataset)   
    
    m1=m.Model(nameAlgorithm,horizon,storeData[0],storeData[1],storeData[2],storeData[3],storeData[4])
    
    displayDataInformations(storeData[5],storeData[6],storeData[7],storeData[0],horizon)    
    displayAlgorithmInformations(nameAlgorithm,m1.getAlgo())
        
    
    
    nbInstances=len(m1.getAlgo().contexts)
        
    #print(str(nbInstances))
    reward=0
    acc=[]
    rwd=[]
    div=[]    
    trial=range(1,m1.getAlgo().horizon+1)
        
    #for j in range (1,self.horizon+1):
    #    trial.append(int(j))
    
    if(sys.argv[4]=="dynamic"):
        nA=nameProcessing(nameAlgorithm)
        setDyn=setDynamicDrawing(horizon,nA,nameDataset)
        displayCRW=setDyn[0]
        displayDiv=setDyn[1]
        displayAcc=setDyn[2
                          ]
    for i in range (0, m1.getAlgo().horizon):                  
        #displayRound(i)         
        data=run(m1,m1.getAlgo(),nbInstances,reward,acc,i,trial,rwd,storeData,div)        
        acc=data[1]
        reward=data[3]
        rwd=data[4]
        div=data[5]
        diversity=data[6]
        accuracy=reward/(i+1)
        if(sys.argv[4]=="dynamic"):
            dynamicDrawing(displayCRW,displayDiv,displayAcc,i,reward,diversity,accuracy)
           
    d2="2D"
    d3="3D"  
    nullTab=[]     
    viewGraphic(data[0],trial,acc,nullTab,"Accuracy","Accuracy evolution over trials",d2)
    viewGraphic(data[3],trial,rwd,nullTab,"Cumulative reward","Cumulative reward evolution over trials",d2)
    viewGraphic(data[6],trial,div,nullTab,"Diversity","Diversity evolution over trials",d2)
    #viewGraphic(str(data[6])+"-"+str(data[0]),acc,div,"Accyracy-Diversity","Diversity evolution over trials")
    viewGraphic(str(data[6])+"-"+str(data[0]),trial,div,acc,"Diversity-Accuracy","Diversity-Accuracy over trials",d3)
    #plot3D(trial,div,acc,"Accuracy Diversity over trials")
    #print(div)
    
def run(m,algo,nbInstances,reward,acc,i,trial,rwd,storeData,div):
         
    idCtx=random.randint(0,nbInstances-1)
    idCtx=random.randint(0, nbInstances-1)
    idCls=algo.chooseAction(idCtx)
    
    nb=[]
    storeData[2].__getitem__(idCls).setSelected()
    #print(str(idCls)+" - "+str(storeData[2].__getitem__(idCls).getSelected()))
    for j in range (0,storeData[1]):
        nb.append(storeData[2].__getitem__(j).getSelected())
    
    
    
    evaluation=float(m.evaluate(idCtx,idCls))
            
    algo.updateReward(idCtx,idCls,evaluation)
    reward+=evaluation
    acc.append(reward/(i+1))
    rwd.append(reward)
    
    cv=variation(nb)
    #print(nb)
    diversity=1-(cv/math.sqrt(storeData[1]))
    div.append(diversity)
    
            
    return reward/algo.horizon,acc,trial,reward,rwd,div,diversity
                  
def setDynamicDrawing(horizon,nA,nameDataset):
    displayCRW=figure(horizon,nA,nameDataset,"Round","Reward","Cumulative rewards: ")
    displayDiv=figure(horizon,nA,nameDataset,"Round","Diversity","Diversity evolution: ")
    #displayDivAcc=figure(horizon,nA,nameDataset,"Accuracy","Diversity","Accuracy and Diversity evolution: ")
    displayAcc=figure(horizon,nA,nameDataset,"Round","Accuracy","Accuracy evolution: ")           
    
    return displayCRW,displayDiv,displayAcc
    
def dynamicDrawing(displayCRW,displayDiv,displayAcc,i,reward,diversity,accuracy):
      dynamicView(displayCRW,i,reward)
      dynamicView(displayDiv,i,diversity)
      #dynamicView(displayDivAcc,diversity,accuracy)
      dynamicView(displayAcc,i,accuracy)
  
    
    

if (len(sys.argv)<5 or len(sys.argv)>=6):
    print (str(sys.argv)+" 4 arguments are needed: name of the dataset (mushrooms, control, or statlog), name of the algorithm (linucb or egreedy), horizon T, and static or dynamic graph drawing")
else:
    print ("You have chosen "+ str(sys.argv[1])+" dataset and "+ str(sys.argv[2]) +" algorithm")
    execute()


