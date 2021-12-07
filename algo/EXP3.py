# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:52:50 2019

@author: gutowski
"""

import math
import random

import numpy as np


class Exp3:

    def __init__(self, horizon, arms, contexts, ratings, gamma):
        self.horizon = horizon
        # TODO fix numpy.array for all algo
        self.arms = np.array(arms)
        self.contexts = contexts
        self.ratings = ratings

        self.weights = np.ones(self.arms.size)
        self.probabilities = np.ones(self.arms.size) / self.arms.size
        self.gamma = gamma
        self.round = 0

    def choose_action(self, _):
        arm = -1
        if self.round < self.arms.size:
            arm = self.round
        else:
            arm = random.choices(range(self.arms.size), weights=self.probabilities, k=1)[0]
        self.round += 1

        return arm

    def update_reward(self, _, arm, evaluation):
        estimated_reward = evaluation / self.probabilities[arm]
        # TODO fix outrange values
        self.weights[arm] = self.weights[arm] * math.exp(estimated_reward * self.gamma / self.arms.size)
        s = np.sum(self.weights)
        for a in range(self.arms.size):
            self.probabilities[a] = (1 - self.gamma) * self.weights[a] / s + self.gamma / self.arms.size
