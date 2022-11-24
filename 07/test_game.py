import game
from game import Rule, Bag

def test_parse():
    bags = []
    rule = Rule('light red bags contain 1 bright white bag, 2 muted yellow bags.', bags)
    assert rule.container == 'light red'
    assert len(rule.content) == 2
    assert rule.content[0][0] == 1
    assert rule.content[0][1].color == 'bright white'
    assert rule.content[1][0] == 2
    assert rule.content[1][1].color == 'muted yellow'

def test_parse_with_no_other():
    bags = []
    rule = Rule('faded blue bags contain no other bags.', bags)
    assert rule.container == 'faded blue'
    assert len(rule.content) == 0

def test_compute_puzzle1():
    bags, _ = game.parse(['light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.'])
    assert game.compute_puzzle1(bags, 'shiny gold') == 4

def test_compute_puzzle2():
    _, rules = game.parse(['light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.'])
    assert game.compute_puzzle2(rules, 'shiny gold') == 32

def test_compute_puzzle2_other_example():
    _, rules = game.parse(['shiny gold bags contain 2 dark red bags.',
    'dark red bags contain 2 dark orange bags.',
    'dark orange bags contain 2 dark yellow bags.',
    'dark yellow bags contain 2 dark green bags.',
    'dark green bags contain 2 dark blue bags.',
    'dark blue bags contain 2 dark violet bags.',
    'dark violet bags contain no other bags.'])
    assert game.compute_puzzle2(rules, 'shiny gold') == 126

def test_add_bag():
    bags = []
    Bag.get(bags, 'dark red')
    assert len(bags) == 1
    