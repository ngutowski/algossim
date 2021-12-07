#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 23:04:19 2019

@author: gutowski
"""

import random

import numpy as np


class Random:
    def __init__(self, horizon, arms, contexts, ratings):
        self.horizon = horizon
        # TODO fix numpy.array for all algo
        self.arms = np.array(arms)
        self.contexts = contexts
        self.ratings = ratings

    def choose_action(self, _):
        return random.randrange(self.arms.size)

    def update_reward(self, _c, _b, _e):
        pass
