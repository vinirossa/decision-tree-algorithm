#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Entropy Functions

    Description...
"""

from math import log2


def information_entropy(prob_list):
    result = 0
    for prob in prob_list:
        if prob != 0:
            result += prob * log2(prob)
    return result if result == 0 else -result


def parent_entropy(dataset, target_index):
    target_node = [e[target_index] for e in dataset]
    parent_probs = []
    for e in sorted(set(target_node)):
        parent_probs.append((sum(x.count(e)
                            for x in dataset)) / len(target_node))
    return information_entropy(parent_probs)


def children_entropy_n_weight(dataset, target_index):
    for row in dataset:

        children_entropies, children_weights = ([] for _ in range(2))

        for index in range(len(row)):
            if index != target_index:

                child_probs, child_entropies, child_weights = (
                    [] for _ in range(3))
                node = [e[index] for e in dataset]
                target_node = [e[target_index] for e in dataset]

                for value in sorted(set(node)):
                    result = 0
                    for e in sorted(set(target_node)):
                        result = (sum(x.count(e)
                                   for x in dataset if x[index] == value)) / node.count(value)
                        child_probs.append(result)
                    child_entropies.append(
                        information_entropy(child_probs))
                    child_weights.append(node.count(value) / len(target_node))

                    child_probs.clear()
            children_entropies.append(child_entropies)
            children_weights.append(child_weights)

    return children_entropies, children_weights


def information_gain(parent_entropy, child_entropies, child_weights):
    sigma = 0
    for (entropy, weight) in zip(child_entropies, child_weights):
        sigma += (entropy * weight)
    result = parent_entropy - sigma
    return result


def get_higher_information_gain(parent_entropy, children_entropies, children_weights):
    igs = []
    for (child_entropies, child_weights) in zip(children_entropies, children_weights):
        igs.append(information_gain(
            parent_entropy, child_entropies, child_weights))

    higher_ig = max(igs)

    if igs.count(higher_ig) > 1:
        print("More than one element with max value. Returning first index and printing duplicated indexes.")
        for index in range(len(igs)):
            if igs[index] == higher_ig:
                print(index)

    higher_ig_index = igs.index(higher_ig)

    return higher_ig, higher_ig_index


if __name__ == "__main__":
    pass
