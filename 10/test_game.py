import game

def test_compute_puzzle1_sample():
    assert game.compute_puzzle1([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]) == 7*5

def test_compute_puzzle1_sample2():
    assert game.compute_puzzle1([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]) == 220

def test_compute_puzzle2_sample():
    assert game.compute_puzzle2([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]) == 8

def test_compute_puzzle2_sample2():
    assert game.compute_puzzle2([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]) == 19208

    