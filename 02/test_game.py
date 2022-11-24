import game

def test_compute_puzzle1():
    assert game.compute_puzzle1(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 2

def test_empty():
    assert game.compute_puzzle1(["        ", ""]) == 0

def test_compute_puzzle2():
    assert game.compute_puzzle2(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]) == 1

    