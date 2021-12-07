# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:51:53 2019

@author: gutowski
"""

import numpy as np


class Ucb1:

    def __init__(self, horizon, arms, contexts, ratings):
        self.horizon = horizon
        # TODO fix numpy.array for all algo
        self.arms = np.array(arms)
        self.contexts = contexts
        self.ratings = ratings

        self.mu_a = np.zeros(self.arms.size)
        self.cumul_reward = np.zeros(self.arms.size)
        self.count_a = np.zeros(self.arms.size)
        self.round = 0

    def choose_action(self, _):
        arm = -1

        if self.round < self.arms.size:
            arm = self.round
        else:
            best = 0
            for a in range(self.arms.size):
                esp = self.mu_a[a] + 2 * np.log(self.round) / self.count_a[a]
                if esp > best:
                    best = esp
                    arm = a
        self.round += 1

        return arm

    def update_reward(self, _, arm, evaluation):
        self.cumul_reward[arm] += evaluation
        self.count_a[arm] += 1
        self.mu_a[arm] = self.cumul_reward[arm] / self.count_a[arm]
