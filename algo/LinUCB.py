# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 2019

@author: gutowski
"""

import numpy as np


class LinUCB:
    def __init__(self, horizon, arms, contexts, ratings, delta):
        self.horizon = horizon
        # TODO fix numpy.array for all algo
        self.arms = np.array(arms)
        self.contexts = contexts
        self.ratings = ratings
        self.delta = delta

        # TODO fix numpy.array for all algo
        self.d = len(self.contexts[0].features)

        self.M = np.zeros((self.arms.size, self.d, self.d))
        self.b = np.zeros((self.arms.size, self.d, 1))

        self.round = 0

        # Not  necessera for LinUCB policy but usefull for knowing the number of selection of each class
        self.count_a = np.zeros(self.arms.size)
        # Not necessar for LinUCB policy but usefull for observing each features density of theta
        self.features_theta = {}

        for a in range(self.arms.size):
            self.M[a] = np.identity(self.d)
            self.features_theta[a] = [[]]

        self.c = np.array(self.contexts)

    @property
    def delta(self):
        return self._delta

    @property
    def alpha(self):
        return self._alpha

    @delta.setter
    def delta(self, d):
        if d == 0:
            self._delta = 0
            self._alpha = 0
        else:
            self._delta = d
            self._alpha = 1 + np.sqrt((np.log(2 / d)) / 2)

    def choose_action(self, context):
        arm = -1

        x = self.get_context(context)

        if self.round < self.arms.size:
            arm = self.round
        else:
            best_pta = 0
            for a in range(self.arms.size):
                ma_inv = np.linalg.inv(self.M[a])
                theta = np.dot(ma_inv, self.b[a])
                pta = np.dot(theta.T, x) + self._alpha * np.sqrt(np.dot(x.T, ma_inv.dot(x)))
                if pta > best_pta:
                    best_pta = pta
                    arm = a
                # TODO check the condition is present in the original paper
                # elif pta == best_pta:
                #     arm = random.randrange(self.arms.size)

        self.round += 1

        return arm

    def update_reward(self, context, arm, evaluation):
        x = self.get_context(context)
        # print(x.T)
        self.M[arm] = self.M[arm] + np.outer(x, x)
        self.b[arm] = self.b[arm] + np.multiply(evaluation, x)

        ainv = np.linalg.inv(self.M[arm])
        theta = np.dot(ainv, self.b[arm])

        # Not necessar for LinUCB policy but usefull for observing each features density of theta
        self.features_theta[arm].append(theta)
        # Not necessar for LinUCB policy but usefull for observing each features density of theta
        self.count_a[arm] += 1

    def get_context(self, context):
        return np.array(self.contexts[context].features).reshape(self.d, 1)
