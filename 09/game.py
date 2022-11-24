def _rule_is_ok(values, value_to_check):
    for index_a, a in enumerate(values):
        for b in values[index_a + 1:]:
            if value_to_check == a + b:
                return True
    return False

def compute_puzzle1(preamble_length, values):
    for index in range(preamble_length, len(values)):
        if not _rule_is_ok(values[index-preamble_length:index], values[index]):
            return values[index]
    return -1

def compute_puzzle2(preamble_length, values):
    value = compute_puzzle1(preamble_length, values)
    print(f'invalid number is {value}')
    end = -1
    for start in range(0, len(values)):
        sum = 0
        offset = 0
        while sum < value or start + offset >= len(values):
            sum += values[start + offset]
            offset += 1
        if sum == value:
            end = start + offset -1
            break
        print(f'... fail')    
    if end == -1:
        return -1
    return min(values[start:end+1]) + max(values[start:end+1])
