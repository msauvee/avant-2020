from typing import List

class Instruction:

    _op: str
    _value: int

    @property
    def op(self):
        return self._op

    @op.setter
    def op(self, op):
        self._op = op

    @property
    def value(self):
        return self._value

    def __init__(self, line: str):
        items = line.split(' ')
        self._op = items[0]
        self._value = int(items[1])

class Program:

    _instructions: List[Instruction]
    _current_instruction_index: int

    @property
    def instructions(self) -> List[Instruction]:
        return self._instructions

    def __init__(self, input: List[str]):
        self._instructions = []
        self._current_instruction_index = 0
        for line in input:
            self._instructions.append(Instruction(line))

    def _run_current_instruction(self):
        current_instruction = self._instructions[self._current_instruction_index]
        if current_instruction.op == 'nop':
            self._current_instruction_index += 1
        elif current_instruction.op == 'jmp':
            self._current_instruction_index += current_instruction.value
        elif current_instruction.op == 'acc':
            self._current_instruction_index += 1
            self._accumulator += current_instruction.value
        else:
            raise ValueError(f'Operation {current_instruction.op} is not supported')
    
    def run(self) -> (bool, int):
        run_instruction_index = []
        self._current_instruction_index = 0
        self._accumulator = 0
        while True:
            run_instruction_index.append(self._current_instruction_index)
            self._run_current_instruction()
            if self._current_instruction_index in run_instruction_index:
                return True, self._accumulator
            if self._current_instruction_index >= len(self._instructions):
                break

        return False, self._accumulator    

def parse(lines) -> Program:
    return Program(lines)

def compute_puzzle1(program: Program) -> (bool, int):
    return program.run()

def compute_puzzle2(program: Program) -> int:
    for instruction in program.instructions:
        if instruction.op != 'nop' and instruction.op != 'jmp':
            continue
        origin_op = instruction.op
        instruction.op = 'nop' if origin_op == 'jmp' else 'jmp'
        loop_detected, accumulator = program.run()
        instruction.op = origin_op
        if not loop_detected:
            return accumulator