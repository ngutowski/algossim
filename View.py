#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:09:11 2019

@author: gutowski
"""


import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from lib.realtimeplot import RealtimePlot

import seaborn as sns


def viewDensity(nbArms,algo,d,nameDataset,viewAll,a):
    
    if(viewAll==1): 
        #print("toto")
        for i in range (0,nbArms):    
            #print("i: "+str(i))
            for f in range (0,d):
                
                tab=[]        
                for z in range (1,int(algo.getSelecteda(i))-1):        
                    tab.append(float(algo.getFeaturesValue(i)[z][f]))
                labelLine="Class: "+str(i)+" - Features: "+str(f)
                if(tab[len(tab)-1]!=0.0):
                    fig=sns.distplot(tab, hist=False,kde=True,kde_kws = {'linewidth': 2},label=labelLine)
        
        #select=range (0,len(tab))
        
        #viewGraphic(0,select,tab,[],"weight","feature convergence","2D")
        plt.xlabel("Theta weights")
        plt.ylabel("Density")
        plt.title("Density per features for each class in "+str(nameDataset))
        plt.show(fig)        
        #print(tab)    
        
    else:
        
        for f in range (0,d):
                
            tab=[]        
            for z in range (1,int(algo.getSelecteda(a))-1):        
                tab.append(float(algo.getFeaturesValue(a)[z][f]))
            labelLine="Classe: "+str(a)+" - Features: "+str(f)
            if(tab[len(tab)-1]!=0.0):
                fig=sns.distplot(tab, hist=False,kde=True,kde_kws = {'linewidth': 2},label=labelLine)
        plt.xlabel("Theta weights")
        plt.ylabel("Density")
        plt.title("Density per features for class "+str(a)  +" in "+str(nameDataset))            
        plt.show(fig)        
        #print(tab)    

                    


def viewGraphic(measure,xTab,yTab,zTab,metric,graphicTitle,dim):
    print("\n"+str(metric) +": "+ str(measure))
    root = tkinter.Tk()
    root.wm_title(graphicTitle)
   
    fig = Figure(figsize=(5, 4), dpi=100)
    
    if (dim=="2D"):
        fig.add_subplot(111,xlabel="Round",ylabel=metric).plot(xTab, yTab)
        
    elif(dim=="3D"):
        ax = fig.gca(projection='3d')    
        ax.plot(xTab, yTab, zTab, label=graphicTitle)
        ax.set_xlabel("Round")
        ax.set_ylabel(metric.split("-")[0])
        ax.set_zlabel(metric.split("-")[1])
        
    
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    if (dim=="3D"):
         ax.mouse_init()
   

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)


        canvas.mpl_connect("key_press_event", on_key_press)


    def _quit():
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)

    tkinter.mainloop()
        # If you put root.destroy() here, it will cause an error if the window is
        # closed with the window manager.    



def displayRound(i):
    if ((i+1)%1000==0 and i>0):
        print("Round -> "+str(i+1))


def displayDataInformations(nbArms,nbContexts,nbPred,dContexts,horizon):
    print("Number of arms: "+str(nbArms))
    print("Number of instances: "+str(nbContexts))
    print("Number of ratings: "+str(nbPred))    
    print("\nNumber of dimensions: "+str(dContexts))
    print("\nHorizon: "+str(horizon))
    
def displayAlgorithmInformations(algoName,algo):
    if (algoName=="linucb"):
        print("\ndelta: "+str(algo.getDelta()))
        print("alpha: "+str(algo.getAlpha()))
    if (algoName=="egreedy"):
        print("\nepsilon: "+str(algo.getEpsilon()))
        
        
        
        
    

def dynamicView(display,i,metric):
    display.add(i+1,metric)
    plt.pause(0.001) 


        
def figure(horizon,nameAlgo,nameData,xl,yl,tl):   
    fig, axes = plt.subplots()
    display = RealtimePlot(axes,horizon)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title(tl+str(nameAlgo)+" - "+str(nameData)+" dataset.")   
         
    return display            





def plot3D(x,y,z,l):
    mpl.rcParams['legend.fontsize'] = 10
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    ax.plot(x, y, z, label=l)
    ax.legend()
    
    plt.show()



def nameProcessing(nameAlgorithm):
     algorithm=nameAlgorithm
     if(algorithm=="random"):
          return nameAlgorithm[0].upper()+nameAlgorithm[1:len(nameAlgorithm)]
               
     if(algorithm=="linucb"):
          return nameAlgorithm[0].upper()+nameAlgorithm[1:3]+nameAlgorithm[3:len(nameAlgorithm)].upper()
            
     if(algorithm=="egreedy"):
          return "epsilon-"+nameAlgorithm[1].upper()+nameAlgorithm[2:3]+nameAlgorithm[3:len(nameAlgorithm)]
          
     if(algorithm=="ucb1"):
          return nameAlgorithm[0:len(nameAlgorithm)].upper()
          
     if(algorithm=="ts"):
          return nameAlgorithm[0:len(nameAlgorithm)].upper()
          
     if(algorithm=="lints"):
          return nameAlgorithm[0].upper()+nameAlgorithm[1:3]+nameAlgorithm[3:len(nameAlgorithm)].upper()
          
     if(algorithm=="exp3"):
          return nameAlgorithm[0:len(nameAlgorithm)].upper()
          
    