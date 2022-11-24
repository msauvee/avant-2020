import game

def test_compute_puzzle1_example():
    group_answers = game.parse(["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b"])
    assert game.compute_puzzle1(group_answers) == 11

def test_compute_puzzle2_example():
    group_answers = game.parse(["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b"])
    assert game.compute_puzzle2(group_answers) == 6

def test_compute_puzzle2_example():
    group_answers = game.parse(["sdxtfzo", "stfzno"])
    assert game.compute_puzzle2(group_answers) == 5


    