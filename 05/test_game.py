import game

def test_compute_puzzle1_FBFBBFFRLR():
    assert game.compute_seat_id("FBFBBFFRLR") == 357

def test_compute_puzzle1_BFFFBBFRRR():
    assert game.compute_seat_id("BFFFBBFRRR") == 567

def test_compute_puzzle1_FFFBBBFRRR():
    assert game.compute_seat_id("FFFBBBFRRR") == 119

def test_compute_puzzle1_BBFFBBFRLL():
    assert game.compute_seat_id("BBFFBBFRLL") == 820

def test_compute_puzzle1():
    assert game.compute_puzzle1(["BFFFBBFRRR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]) == 820

    