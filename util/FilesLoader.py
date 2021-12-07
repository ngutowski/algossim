# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:27:59 2019

@author: gutowski
"""

from data.Dataset import Arm, Context


class FilesLoader:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    def __init__(self, file_name):
        self.fileName = file_name

    def loadFile(self):
        # print("Loading file:"+str(self.fileName)+"..."+"\n")
        return open(self.fileName)

    def processFileArms(self, f):

        print("Loading " + str(self.fileName))
        arms = []
        nb_arms = 0
        for line in f:
            tableau = line.split(";")
            size = len(tableau)
            features = [0] * (size - 2)
            d_bras = size - 2
            nb_arms += 1
            ida = tableau[0]
            name = tableau[1]

            for i in range(2, size):
                features[i - 2] = tableau[i].strip()

            arms.append(Arm(ida, features, name))

        return d_bras, nb_arms, arms

    def processFileContexts(self, f):

        print("Loading " + str(self.fileName))
        contexts = []
        nb_contexts = 0
        for line in f:
            tableau = line.split(";")
            size = len(tableau)
            features = [0] * (size - 2)
            d_contexts = size - 2
            nb_contexts += 1
            ida = tableau[0]

            for i in range(1, size - 1):
                features[i - 1] = float(tableau[i].strip())

            contexts.append(Context(ida, features))

        return d_contexts, nb_contexts, contexts

    def processFileRatings(self, f, _, __):

        print("Loading " + str(self.fileName))
        ratings = dict()

        nb_ratings = 0
        for line in f:
            tableau = line.split(";")
            nb_ratings += 1
            id_ctx = tableau[0]
            id_arm = tableau[1]
            ratings[id_ctx, id_arm] = tableau[2]

        return ratings, nb_ratings

    def processFile(self, f):

        print("Loading " + str(self.fileName))
        for line in f:
            tableau = line.split(";")
            # print(tableau[127])
            d = len(tableau)
            # for value in tableau:
            # print(str(value[-1]))
        return d

    @staticmethod
    def close(f):
        f.close()
