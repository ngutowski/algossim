#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:11:08 2019

@author: gutowski
"""
from algo.EXP3 import Exp3
from algo.Egreedy import Egreedy
from algo.LinTS import LinearThompsonSampling
from algo.LinUCB import LinUCB
from algo.Random import Random
from algo.TS import ThompsonSampling
from algo.UCB1 import Ucb1


class Model:

    def __init__(self, model_name, horizon, arms, contexts, ratings):

        self.ratings = ratings
        self.horizon = horizon

        gamma = delta = epsilon = 0.1

        if model_name == "random":
            self.model = Random(horizon, arms, contexts, ratings)

        elif model_name == "linucb":
            self.model = LinUCB(horizon, arms, contexts, ratings, delta)

        elif model_name == "egreedy":
            self.model = Egreedy(horizon, arms, contexts, ratings, epsilon)
        elif model_name == "ucb1":
            self.model = Ucb1(horizon, arms, contexts, ratings)
        elif model_name == "ts":
            self.model = ThompsonSampling(horizon, arms, contexts, ratings)

        elif model_name == "lints":
            self.model = LinearThompsonSampling(horizon, arms, contexts, ratings, delta, 0.01)

        elif model_name == "exp3":
            self.model = Exp3(horizon, arms, contexts, ratings, gamma)

    def evaluate(self, context, arm):
        evaluation = self.ratings[str(context), str(arm)]
        return evaluation
