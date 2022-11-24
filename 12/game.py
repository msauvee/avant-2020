from enum import Enum
from typing import List

class Boat:

    @property
    def position(self):
        return self._position

    @property
    def waypoint(self):
        return self._waypoint

    def __init__(self, waypoint):
        self._waypoint = waypoint
        self._position = [0, 0]

    def _navigate(self, instruction: str, strategy):
        self._position, self._waypoint = strategy(self, instruction)

    def navigate(self, instructions: List[str], strategy) -> int:
        for instruction in instructions:
            self._navigate(instruction, strategy)
        return abs(self._position[0]) + abs(self._position[1])

def strategy_puzzle1(boat: Boat, instruction: str) -> (List[int], List[int]):
    op = instruction[0:1]
    count = int(instruction[1:])
    position = boat.position
    waypoint = boat.waypoint
    if op == 'N':
        position[0] += count
    elif op == 'S':
        position[0] -= count
    elif op == 'E':
        position[1] += count
    elif op == 'W':
        position[1] -= count
    elif op == 'L':
        waypoint = _turn_left(waypoint, count)
    elif op == 'R':
        waypoint = _turn_left(waypoint, 360-count)
    elif op == 'F':
        position[0] += count * waypoint[0]
        position[1] += count * waypoint[1]
    return position, waypoint    

def _turn_left_90(waypoint: List[int]) -> List[int]:
    return [waypoint[1], -waypoint[0]]

def _turn_left(waypoint: List[int], count) -> List[int]:
    for _ in range(int(count/90)):
        waypoint = _turn_left_90(waypoint)
    return waypoint

def strategy_puzzle2(boat: Boat, instruction: str) -> (List[int], int, List[int]):
    op = instruction[0:1]
    count = int(instruction[1:])
    position = boat.position
    waypoint = boat.waypoint
    if op == 'N':
        waypoint[0] += count
    elif op == 'S':
        waypoint[0] -= count
    elif op == 'E':
        waypoint[1] += count
    elif op == 'W':
        waypoint[1] -= count
    elif op == 'L':
        waypoint = _turn_left(waypoint, count)
    elif op == 'R':
        waypoint = _turn_left(waypoint, 360-count)
    elif op == 'F':
        position[0] += count * waypoint[0]
        position[1] += count * waypoint[1]
    return position, waypoint    

def compute_puzzle1(instructions: List[str]) -> int:
    boat = Boat([0,1])
    return boat.navigate(instructions, strategy_puzzle1)

def compute_puzzle2(instructions: List[str]) -> int:
    boat = Boat([1, 10])
    return boat.navigate(instructions, strategy_puzzle2)