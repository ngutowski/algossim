#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:27:59 2019

@author: gutowski
"""

from data.Dataset import Arm,Context

class FilesLoader:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    
    def __init__(self,fileName):    
        self.fileName = fileName
        
        
    def loadFile(self):
    
        #print("Loading file:"+str(self.fileName)+"..."+"\n")

        c = self.fileName
        f=open(c)
    		
        return f
    

    def processFileArms(self,f):
        
        print("Loading "+str(self.fileName))
        arms=[]
        nbBras=0
        for line in f:
            tableau=line.split(";")
            size=len(tableau)        
            features=[0]*(size-2)           
            dBras=size-2
            nbBras+=1
            id=tableau[0]
            name=tableau[1]
        
            for i in range (2,size):
                features[i-2]=tableau[i].strip()
                
                    
            arms.append(Arm(id, features, name))
        
        return dBras,nbBras,arms


    def processFileContexts(self,f):
        
        print("Loading "+str(self.fileName))
        contexts=[]
        nbContexts=0
        for line in f:
            tableau=line.split(";")
            size=len(tableau)        
            features=[0]*(size-2)           
            dContexts=size-2	
            nbContexts+=1
            id=tableau[0]
                   
            for i in range (1,size-1):
                features[i-1]=float(tableau[i].strip())                
                    
            contexts.append(Context(id, features))
        
        return dContexts,nbContexts,contexts

    def processFileRatings(self,f,nbContexts,nbArms):
        
        print("Loading "+str(self.fileName))
        ratings=dict()
        
        nbRatings=0
        for line in f:
            tableau=line.split(";")
            nbRatings+=1
            idCtx=tableau[0]
            idArm=tableau[1]       
            ratings[idCtx,idArm]=tableau[2]                
                    
            
        
        return ratings,nbRatings

    

    def processFile(self,f):
        
        print("Loading "+str(self.fileName))
        for line in f:
            tableau=line.split(";")
            #print(tableau[127])
            d=len(tableau)	
            #for value in tableau:
                #print(str(value[-1]))
        return d


    def count(self,f):
        compteur=0
        for line in f:
            compteur+=1
        return compteur
    
    def close(self,f):
       f.close()
