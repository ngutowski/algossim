# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 2019

@author: gutowski
"""

import math

import numpy as np


class LinearThompsonSampling:

    def __init__(self, horizon, arms, contexts, ratings, delta, r):
        self.horizon = horizon
        # TODO fix numpy.array for all algo
        self.arms = np.array(arms)
        self.contexts = contexts
        self.ratings = ratings
        self.delta = delta

        # TODO fix numpy.array for all algo
        self.d = len(self.contexts[0].features)

        self.B = np.zeros((self.arms.size, self.d, self.d))
        self.f = np.zeros((self.arms.size, self.d, 1))
        self.v2 = math.pow(r * math.sqrt(9 * self.d * math.log(horizon / delta)), 2)

        self.round = 0

        for a in range(self.arms.size):
            self.B[a] = np.identity(self.d)
            self.f[a] = np.zeros((self.d, 1)).astype(float)

    def choose_action(self, context):
        arm = -1

        x = self.get_context(context)
        if self.round < self.arms.size:
            arm = self.round
        else:
            best_rw = 0
            for a in range(self.arms.size):
                ba_inv = np.linalg.inv(self.B[a])
                ba_inv_v2 = np.multiply(ba_inv, self.v2)
                mu = np.ndarray.flatten(np.dot(ba_inv, self.f[a]))
                sample = np.random.multivariate_normal(mu, ba_inv_v2)
                rw_exp = np.absolute(np.dot(sample.T, x))
                # TODO inspect equality
                if rw_exp > best_rw:
                    best_rw = rw_exp
                    arm = a
                # TODO check the condition is present in the original paper
                # Choose randomly the best arm ?
                # elif rw_exp == best:
                #
        self.round += 1

        return arm

    def update_reward(self, context, arm, evaluation):
        x = self.get_context(context)
        self.B[arm] = self.B[arm] + np.outer(x, x)
        self.f[arm] = self.f[arm] + np.multiply(evaluation, x)

    def get_context(self, context):
        return np.array(self.contexts[context].features).reshape(self.d, 1)
