def _compute(input, lower, upper):
    min = 0
    max = pow(2,len(input))
    for  char in input:
        if char == lower:
            max = min + (max - min) / 2
        if char == upper:
            min = max - (max - min) / 2
    return int(min)

def compute_seat_id(boarding):
    return int(_compute(boarding[0:7], 'F', 'B') * 8 + _compute(boarding[7:], 'L', 'R'))

def compute_puzzle1(boardings):
    max = None
    for boarding in boardings:
        seat_id = compute_seat_id(boarding)
        if max is None or seat_id > max:
            max = seat_id
    return max

def compute_puzzle2(boardings):
    min = None
    max = None
    seat_ids = []
    for boarding in boardings:
        seat_id = compute_seat_id(boarding)
        if max is None or seat_id > max:
            max = seat_id
        if min is None or seat_id < min:
            min = seat_id
        seat_ids.append(seat_id)
    # create a list of missing that will be reduced
    missing = []
    for i in range (min, max+1):
        missing.append(i)
    # reduce with known saet_ids
    for seat_id in seat_ids:
        missing.remove(seat_id)
    assert len(missing) == 1
    return missing[0]