#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 23:21:27 2019

@author: gutowski
"""

import util.FilesLoader as fl

def dataStore(nameDataset):
    a="./data/%s/classes.txt"%nameDataset
    x="./data/%s/descriptions.txt"%nameDataset
    p="./data/%s/predictions.txt"%nameDataset
        
    fArms=fl.FilesLoader(a)
    storeArms=fArms.loadFile()    
    arms=[]    
    resArms=fArms.processFileArms(storeArms)    
    arms=resArms[2]
    nbArms=resArms[1]
    dArms=resArms[0]
        
    #print(arms[0].getArmId())
    #print(arms[0].getArmName())
    #print(arms[0].getArmFeat())
    
    
    
    fContexts=fl.FilesLoader(x)
    storeContexts=fContexts.loadFile()
    contexts=[]    
    resContexts=fContexts.processFileContexts(storeContexts)    
    contexts=resContexts[2]
    nbContexts=resContexts[1]
    dContexts=resContexts[0]
       
    #print(contexts[0].getContextId())
    #print(contexts[0].getContextFeat())
         
        
    fRatings=fl.FilesLoader(p)
    storeRatings=fRatings.loadFile()
        
        
    ratings=dict()
    resRatings=fRatings.processFileRatings(storeRatings,nbContexts,nbArms)
        
    ratings=resRatings[0]
    nbPred=resRatings[1]
        
    #print(ratings)
               
        
    fArms.close(storeArms)
    fRatings.close(storeRatings)
    fContexts.close(storeContexts)
        
    return dContexts,nbArms,arms,contexts,ratings,nbArms,nbContexts,nbPred,dArms