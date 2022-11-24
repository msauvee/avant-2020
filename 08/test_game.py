import game

def test_compute_puzzle1_on_sample():
    program = game.parse(['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6'])
    loop_detected, accumultaor = game.compute_puzzle1(program)
    assert loop_detected
    assert accumultaor == 5

def test_compute_puzzle2_on_sample():
    program = game.parse(['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6'])
    assert game.compute_puzzle2(program) == 8


    