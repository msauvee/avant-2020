import game

def test_compute_puzzle1():
    assert game.compute_puzzle1(['F10','N3','F7','R90','F11']) == 25

def test_compute_puzzle2():
    assert game.compute_puzzle2(['F10','N3','F7','R90','F11']) == 286


    