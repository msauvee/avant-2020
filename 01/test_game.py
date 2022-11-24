import game

def test_find2():
    assert game.find2([1721,979,366,299,675,1456]) == 514579

def test_one_value_in_find2():
    assert game.find2([10]) == -1

def test_no_answer_in_find2():
    assert game.find2([10, 20]) == -1

def test_find3():
    assert game.find3([1721,979,366,297,2,675,1456]) == 1022274

def test_one_value_in_find3():
    assert game.find3([10]) == -1

def test_one_value_in_find3():
    assert game.find3([10, 20]) == -1

def test_no_answer_in_find3():
    assert game.find3([10, 20, 30]) == -1