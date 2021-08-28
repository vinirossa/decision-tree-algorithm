#!/usr/bin/env python

__author__ = "Vinícius Pereira"
__copyright__ = "Copyright 2021, Vinícius Pereira"
__credits__ = "Vinícius Pereira"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Vinícius Pereira"
__email__ = "viniciuspsb@gmail.com"
__status__ = "Development"

import sys
import os
import math as m
import inspect as ins


def artificial_intelligence(index):
    # try:
    dataset = [["alto", "longe", "interessante", "sim"],
               ["baixo", "perto", "desinteressante", "não"],  # não
               ["baixo", "longe", "interessante", "sim"],
               ["alto", "longe", "desinteressante", "não"],  # não
               ["alto", "perto", "interessante", "sim"],  # sim
               ["baixo", "longe", "desinteressante", "não"]]  # nao

    def information_entropy(probs):
        res = 0
        for prob in probs:
            if prob != 0:
                res += prob * m.log2(prob)
        return res if res == 0 else -res

    def information_gain(father_entropy, child_weights, child_entropies):
        sigma = 0
        for (weight, entropy) in zip(child_weights, child_entropies):
            sigma += (weight * entropy)
        res = father_entropy - sigma
        return res

    target = [e[3] for e in dataset]
    father_probs = []
    for e in list(set(target)):
        father_probs.append((sum(x.count(e) for x in dataset)) / len(target))
    father_entropy = information_entropy(father_probs)

    target = [e[3] for e in dataset]
    column1 = [e[index] for e in dataset]
    child_probs = []
    child_entropies = []
    child_weights = []

    for v in list(set(column1)):
        res = 0
        for e in list(set(target)):
            res = (sum(x.count(e)
                       for x in dataset if x[index] == v)) / column1.count(v)
            child_probs.append(res)
        child_entropies.append(information_entropy(child_probs))
        child_weights.append(column1.count(v) / len(target))
        print(child_probs)
        child_probs.clear()

    ig = information_gain(father_entropy, child_weights, child_entropies)

    print(list(set(target)))
    print(list(set(column1)))
    print("Father Probs:", father_probs)
    print("Father Entropy:", father_entropy)
    print("Child Probs:", child_probs)
    print("Child Entropies:", child_entropies)
    print("Child Weights:", child_weights)
    print("Infomation Gain:", ig)

    # except BaseException as e:
    #     print("--- Execution Error ---")
    #     print("File:", os.path.basename(__file__))
    #     print("Line:", ins.currentframe().f_lineno-4)
    #     print("Class:", e.__class__.__name__)
    #     print("Info:", e.__doc__)


if __name__ == "__main__":
    artificial_intelligence(2)
