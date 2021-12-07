# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:37:44 2019

@author: gutowski
"""
import math
import random
import sys

from scipy.stats import variation

import View
from Model import Model
from data.DataMonitor import data_store


# from View import plot3D


def execute(name_dataset=str(sys.argv[1]), name_algorithm=str(sys.argv[2]), horizon=int(sys.argv[3])):
    # seed = 0
    # random.seed(seed)
    # np.random.seed(seed)

    store_data = data_store(name_dataset)

    (dContexts, nbArms, arms, contexts, ratings, nbArms, nbContexts, nbPred, dArms) = store_data

    m1 = Model(name_algorithm, horizon, arms, contexts, ratings)

    View.displayDataInformations(nbArms, nbContexts, nbPred, dContexts, horizon)
    View.displayAlgorithmInformations(name_algorithm, m1.model)

    nb_instances = len(m1.model.contexts)

    # print(str(nb_instances))
    reward = 0
    acc = []
    rwd = []
    div = []
    trial = range(1, m1.model.horizon + 1)

    # for j in range (1,self.horizon+1):
    #    trial.append(int(j))

    if sys.argv[4] == "dynamic":
        set_dyn = set_dynamic_drawing(horizon, View.nameProcessing(name_algorithm), name_dataset)
        display_crw = set_dyn[0]
        display_div = set_dyn[1]
        display_acc = set_dyn[2]
    for i in range(m1.model.horizon):
        View.displayRound(i)
        data = run(m1, m1.model, nb_instances, reward, acc, i, trial, rwd, store_data, div)
        acc = data[1]
        reward = data[3]
        rwd = data[4]
        div = data[5]
        diversity = data[6]
        accuracy = reward / (i + 1)
        if sys.argv[4] == "dynamic":
            dynamic_drawing(display_crw, display_div, display_acc, i, reward, diversity, accuracy)

    d2 = "2D"
    d3 = "3D"
    null_tab = []
    # View accuracy evolution over rounds
    View.viewGraphic(data[0], trial, acc, null_tab, "Accuracy", "Accuracy evolution over trials", d2)

    # View Cumulative Reward evolution over rounds
    View.viewGraphic(data[3], trial, rwd, null_tab, "Cumulative reward", "Cumulative reward evolution over trials", d2)

    # View Diversity evolution over rounds
    View.viewGraphic(data[6], trial, div, null_tab, "Diversity", "Diversity evolution over trials", d2)

    # viewGraphic(str(data[6])+"-"+str(data[0]),acc,div,"Accyracy-Diversity","Diversity evolution over trials")

    # View Accuracy-Diversity evolution over rounds
    View.viewGraphic(str(data[6]) + "-" + str(data[0]), trial, div, acc, "Diversity-Accuracy",
                     "Diversity-Accuracy over trials", d3)

    # View density of each feature for each arm in LinUCB only (very unreadable if too many features or classes) try
    # it with control and controlsp viewDensity(nbArms,m1.getAlgo(),dContexts,nameDataset,1,0)

    # View densitiy for each features in class 0 in LinUCB only
    # viewDensity(nbArms,m1.getAlgo(),dContexts,nameDataset,0,0)

    # View densitiy for each features in class 1 in LinUCB only
    # viewDensity(nbArms,m1.getAlgo(),dContexts,nameDataset,0,1)


def run(m, algo, nb_instances, reward, acc, i, trial, rwd, store_data, div):
    context = random.randint(0, nb_instances - 1)
    cls = algo.choose_action(context)

    nb = []
    store_data[2].__getitem__(cls).count += 1
    # print(str(cls)+" - "+str(storeData[2].__getitem__(cls).getSelected()))
    for j in range(0, store_data[1]):
        nb.append(store_data[2].__getitem__(j).count)

    evaluation = float(m.evaluate(context, cls))

    algo.update_reward(context, cls, evaluation)
    reward += evaluation
    acc.append(reward / (i + 1))
    rwd.append(reward)

    cv = variation(nb)
    # print(nb)
    diversity = 1 - (cv / math.sqrt(store_data[1]))
    div.append(diversity)

    return reward / algo.horizon, acc, trial, reward, rwd, div, diversity


def set_dynamic_drawing(horizon, na, name_dataset):
    display_crw = View.figure(horizon, na, name_dataset, "Round", "Reward", "Cumulative rewards: ")
    display_div = View.figure(horizon, na, name_dataset, "Round", "Diversity", "Diversity evolution: ")
    # displayDivAcc=figure(horizon,nA,nameDataset,"Accuracy","Diversity","Accuracy and Diversity evolution: ")
    display_acc = View.figure(horizon, na, name_dataset, "Round", "Accuracy", "Accuracy evolution: ")

    return display_crw, display_div, display_acc


def dynamic_drawing(display_crw, display_div, display_acc, i, reward, diversity, accuracy):
    View.dynamicView(display_crw, i, reward)
    View.dynamicView(display_div, i, diversity)
    # dynamicView(displayDivAcc,diversity,accuracy)
    View.dynamicView(display_acc, i, accuracy)


if __name__ == '__main__':
    if len(sys.argv) < 5 or len(sys.argv) >= 6:
        print(str(
            sys.argv) + "4 arguments are needed: name of the dataset (mushrooms, control, or statlog), name of the "
                        "algorithm (linucb or egreedy), horizon T, and static or dynamic graph drawing")
    else:
        print("You have chosen " + str(sys.argv[1]) + " dataset and " + str(sys.argv[2]) + " algorithm")
        execute()
