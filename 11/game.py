from enum import Enum, auto
import sys

class Seat(Enum):
    FLOOR = '.'
    EMPTY = 'L'
    OCCUPIED = '#'

class Area:
    @property
    def occupied_seats_count(self):
        count = 0
        for row in self._seats:
            for seat in row:
                count += 1 if seat == Seat.OCCUPIED else 0
        return count 

    def __init__(self, lines):
        self._seats = []
        for line in lines:
            row_seats = []
            for character in line:
                if character == Seat.EMPTY.value:
                    row_seats.append(Seat.EMPTY)
                if character == Seat.FLOOR.value:
                    row_seats.append(Seat.FLOOR)
            self._seats.append(row_seats)

    def _has_neighboor(self, row, column):
        return 1 if row >= 0 and row < len(self._seats) and column >= 0 and column < len(self._seats[row]) and self._seats[row][column] == Seat.OCCUPIED else 0

    def get_immediate_neighboor(self, row, column):
        return self._has_neighboor(row-1, column-1) \
        + self._has_neighboor(row-1, column) \
        + self._has_neighboor(row-1, column+1) \
        + self._has_neighboor(row, column-1) \
        + self._has_neighboor(row, column+1) \
        + self._has_neighboor(row+1, column-1) \
        + self._has_neighboor(row+1, column) \
        + self._has_neighboor(row+1, column+1) 

    def _see_neighboor(self, row, row_offset, column, column_offset):
        row += row_offset
        column += column_offset
        while row >= 0 and row < len(self._seats) and column >= 0 and column < len(self._seats[row]):
            if self._seats[row][column] == Seat.EMPTY:
                return 0
            if self._seats[row][column] == Seat.OCCUPIED:
                return 1
            row += row_offset
            column += column_offset
        return 0

    def get_viewed_neighboor(self, row, column):
        return self._see_neighboor(row, -1, column, -1) \
        + self._see_neighboor(row, -1, column,  0) \
        + self._see_neighboor(row, -1, column, +1) \
        + self._see_neighboor(row,  0, column, -1) \
        + self._see_neighboor(row,  0, column, +1) \
        + self._see_neighboor(row, +1, column, -1) \
        + self._see_neighboor(row, +1, column,  0) \
        + self._see_neighboor(row, +1, column, +1) 

    def run(self, strategy) -> int:
        change_count = 0
        new_seats = []
        for i, row in enumerate(self._seats):
            new_row = []
            new_seats.append(new_row)
            for j, seat in enumerate(row):
                new_seat, count = strategy(self, seat, i, j)
                new_row.append(new_seat)
                change_count += count

        self._seats = new_seats
        #for i, row in enumerate(self._seats):       
        #    for j, seat in enumerate(row):
        #        sys.stdout.write(seat.value)
        #    sys.stdout.write('\n')
        #sys.stdout.write('\n')

        return change_count

def puzzle1_startegy(area, seat, row, column) -> (Seat, int):
    change_count = 0
    neighbour = area.get_immediate_neighboor(row, column)
    if seat == Seat.EMPTY and neighbour == 0:
        seat = Seat.OCCUPIED
        change_count += 1
    elif seat == Seat.OCCUPIED and neighbour >= 4:
        seat = Seat.EMPTY
        change_count += 1
    return seat, change_count

def puzzle2_startegy(area, seat, row, column) -> (Seat, int):
    change_count = 0
    neighbour = area.get_viewed_neighboor(row, column)
    if seat == Seat.EMPTY and neighbour == 0:
        seat = Seat.OCCUPIED
        change_count += 1
    elif seat == Seat.OCCUPIED and neighbour >= 5:
        seat = Seat.EMPTY
        change_count += 1
    return seat, change_count

def parse(lines):
    return Area(lines)

def compute_puzzle1(area: Area) -> int:
    while area.run(puzzle1_startegy) > 0:
        pass
    return area.occupied_seats_count

def compute_puzzle2(area: Area) -> int:
    while area.run(puzzle2_startegy) > 0:
        pass
    return area.occupied_seats_count