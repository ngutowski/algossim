#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:48:46 2019

@author: gutowski
"""




class Arm:
	def __str__(self):
		return "armId: "+str(self.armId)+" - Name: '"+self.armName+"'"

	def __init__(self, id, features, name):
		self.armId = id
		self.armFeat = features
		self.armName = name
		self.selected=0
        

	def getArmId(self):
		return self.armId
	
	def getArmName(self):
		return self.armName
	
	def getArmFeat(self):
		return self.armFeat
    
	def getSelected(self):
		return self.selected
	def setSelected(self):
		self.selected+=1
	

class Context:
	def __str__(self):
		return "contextId: "+str(self.contextId)

	def __init__(self, id, features):
		self.contextId = id
		self.contextFeat = features


	def getContextId(self):
		return self.contextId
	
	def getContextFeat(self):
		return self.contextFeat
	
	


        
        
        
        
        
        
