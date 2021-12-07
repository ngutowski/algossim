# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:42:01 2019

@author: gutowski
"""

import random

import numpy as np


class Egreedy:

    def __init__(self, horizon, arms, contexts, ratings, epsilon):
        self.horizon = horizon
        # TODO fix numpy.array for all algo
        self.arms = np.array(arms)
        self.contexts = contexts
        self.ratings = ratings
        self.epsilon = epsilon

        self.mu_a = np.zeros(self.arms.size)
        self.cumul_reward = np.zeros(self.arms.size)
        self.count_a = np.zeros(self.arms.size)
        self.round = 0

    def choose_action(self, _):
        arm = -1

        if self.round < self.arms.size:
            arm = self.round
        else:
            best_mu_a = 0
            for a in range(self.arms.size):
                if self.epsilon <= random.uniform(0, 1):
                    if self.mu_a[a] > best_mu_a:
                        best_mu_a = self.mu_a[a]
                        arm = a
                else:
                    arm = random.randrange(self.arms.size)
        self.round += 1

        return arm

    def update_reward(self, _, arm, evaluation):
        # TODO check the condition is present in the original paper
        # if evaluation >= 1:
        self.cumul_reward[arm] += evaluation
        self.count_a[arm] += 1
        self.mu_a[arm] = self.cumul_reward[arm] / self.count_a[arm]
