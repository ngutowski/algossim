"""
Created on Sat Aug 17 23:52:14 2019

@author: gutowski
"""

import random

import numpy as np


class ThompsonSampling:

    def __init__(self, horizon, arms, contexts, ratings):
        self.horizon = horizon
        # TODO fix numpy.array for all algo
        self.arms = np.array(arms)
        self.contexts = contexts
        self.ratings = ratings

        self.mu_a = np.zeros(self.arms.size)
        self.cumul_rewards = np.zeros(self.arms.size)
        self.cumul_regrets = np.zeros(self.arms.size)
        self.count_a = np.zeros(self.arms.size)
        self.round = 0

    def choose_action(self, _):
        arm = -1

        if self.round < self.arms.size:
            arm = self.round
        else:
            best = 0
            for a in range(self.arms.size):
                sample = random.betavariate(self.cumul_rewards[a] + 1, self.cumul_regrets[a] + 1)
                if sample > best:
                    best = sample
                    arm = a
        self.round += 1

        return arm

    def update_reward(self, _, arm, evaluation):
        if evaluation >= 1:
            self.cumul_rewards[arm] += 1
        else:
            self.cumul_regrets[arm] += 1
