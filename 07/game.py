from __future__ import annotations
from typing import List

class Bag:

    @property
    def color(self):
        return self._color

    @property
    def rules(self) -> List[Rule]:
        return self._rules

    def __init__(self, color):
        self._color = color
        self._rules = []

    def add_rule(self,rule):
        self.rules.append(rule)

    @staticmethod
    def find(bags, color):
        for bag in bags:
            if bag.color == color:
                return bag
        return None

    @staticmethod
    def get(bags, color):
        for bag in bags:
            if bag.color == color:
                return bag
        bag = Bag(color)
        bags.append(bag)
        return bag


class Rule:
    
    @property
    def container(self) -> str:
        return self._container

    @property
    def content(self):
        return self._content

    def recurrent_content_count(self, rules):
        count = 1
        for item in self._content:
            count += item[0] * Rule.find(item[1].color, rules).recurrent_content_count(rules)
        return count

    @staticmethod
    def find(color, rules):
        for rule in rules:
            if rule._container == color:
                return rule

    def __init__(self, input, bags: List[Bag]):
        items = input.split(' bags contain ')
        self._container = items[0]
        content = items[1].split(', ')
        self._content = []
        for item in content:
            words = item.split(' ')
            words.pop(len(words)-1)
            if words[0] != 'no':
                color = ' '.join(words[1:])
                bag = Bag.get(bags, color)
                self._add_content(int(words[0]), bag)

    def _add_content(self, count: int, bag: Bag):
        self._content.append((count, bag))
        bag.add_rule(self)


def parse(values):
    rules = []
    bags = []
    for value in values:
        rules.append(Rule(value, bags))
    return bags, rules

def _find_new_containers(color, colors, bags):
    new_colors = []
    for bag in bags:
        if bag.color == color:
            for rule in bag.rules:
                if not rule.container in colors:
                    new_colors.append(rule.container)
    return new_colors

def compute_puzzle1(bags: List[Bag], color):
    processed_colors = [color]
    colors = [color]
    result = []
    while True:
        new_colors = []
        for color in  colors:
            for new_color in _find_new_containers(color, processed_colors, bags):
                if not new_color in new_colors:
                    new_colors.append(new_color)
        if len(new_colors) == 0:
            break
        result.extend(new_colors)
        processed_colors.extend(new_colors)
        colors = new_colors
    return len(result)

def compute_puzzle2(rules: List[Rule], color):
    return Rule.find(color, rules).recurrent_content_count(rules) - 1