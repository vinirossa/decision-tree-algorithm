#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Entropy Decision Tree

    Description...
"""

import entropy_functions as entf


def entropy_decision_tree(dataset: list, target_index: int):
    # try:
    print("\n---- Entropy Decision Tree ----")

    parent_entropy = entf.parent_entropy(dataset, target_index)

    children_entropies, children_weights = entf.children_entropy_n_weight(
        dataset, target_index)
    print("Children entropies:", children_entropies)
    print("Children weights:", children_weights)

    higher_ig, higher_ig_index = entf.get_higher_information_gain(
        parent_entropy, children_entropies, children_weights)
    print("Higher IG:", higher_ig)
    print("Higher IG Index:", higher_ig_index)


if __name__ == "__main__":

    dataset = [["alto", "longe", "interessante", "sim"],
               ["baixo", "perto", "desinteressante", "não"],
               ["baixo", "longe", "interessante", "sim"],
               ["alto", "longe", "desinteressante", "não"],
               ["alto", "perto", "interessante", "sim"],
               ["baixo", "longe", "desinteressante", "não"]]

    entropy_decision_tree(dataset, target_index=3)
