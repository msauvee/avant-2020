from typing import List
import sys

def _max_distance(values: List[int], device):
    max = 0
    current = 0
    for index in range(0, len(values)):
        if values[index] - current > max:
            max = values[index] - current
        current = values[index]
    return max if device - current < max else device - current

def compute_puzzle1(values):
    values.sort()
    assert values[0] == 1 or values[0] == 3
    one_jolt_count = 1 if values[0] == 1 else 3
    three_jolt_count = 1
    for index in range(0, len(values)-1):
        diff = values[index+1] - values[index]
        if diff == 1:
            one_jolt_count += 1
        if diff == 3:
            three_jolt_count += 1
    return one_jolt_count * three_jolt_count

class Node:
    @property
    def value(self):
        return self._value

    @property
    def child_count(self):
        return len(self._sub_nodes)

    @property
    def nb_combination(self):
        if self._nb_combination:
            return self._nb_combination

        if len(self._sub_nodes) == 0:
            return 1
        count = 0
        for node in self._sub_nodes:
            count += node.nb_combination

        self._nb_combination = count
        return self._nb_combination

    def __init__(self,value):
        self._value = value
        self._sub_nodes = []
        self._nb_combination = None

    def link(self, linked_node):
        self._sub_nodes.append(linked_node) 
    

def compute_puzzle2(values):
    values.append(0)
    values.sort()
    values.append(values[-1] + 3)
    adapters = []
    for value in values:
        adapters.append(Node(value))
    
    for index, adapter in enumerate(adapters):
        for i in range(1, 4):
            if index + i < len(adapters) and adapters[index + i].value - adapters[index].value <= 3:
                adapter.link(adapters[index + i])

    return adapters[0].nb_combination