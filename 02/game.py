

def _parse_policyAndPassword(policyAndPassword):
    tokens = policyAndPassword.split(' ')
    if len(tokens) != 3:
        raise ValueError(f'{policyAndPassword} is not a valid input')
    
    minAndMax = tokens[0].split('-')
    if len(minAndMax) != 2:
        raise ValueError(f'{tokens[0]} is not a valid for range')
    min = int(minAndMax[0])
    max = int(minAndMax[1])
    if len(tokens[1]) != 2:
        raise ValueError(f'{tokens[1]} is not a valid for letter (with :)') 
    letter = tokens[1][0]
    password = tokens[2]
    return min, max, letter, password

def _is_valid_puzzle1(policyAndPassword):
    min, max, letter, password = _parse_policyAndPassword(policyAndPassword)
    count = password.count(letter)
    return count >= min and count <= max

def _is_valid_puzzle2(policyAndPassword):
    min, max, letter, password = _parse_policyAndPassword(policyAndPassword)
    if (min > len(password) or max > len(password)):
        raise ValueError(f'{policyAndPassword} is not a valid input, position out of range')
    return bool(password[min-1]==letter) ^ bool(password[max-1]==letter)

def _validate(policiesAndPasswords, validator):
    count = 0
    for policyAndPassword in policiesAndPasswords:
        policyAndPassword = policyAndPassword.strip()
        if len(policyAndPassword)>0 and validator(policyAndPassword):
            count += 1
    return count

def compute_puzzle1(policiesAndPasswords):
    return _validate(policiesAndPasswords, _is_valid_puzzle1)

def compute_puzzle2(policiesAndPasswords):
    return _validate(policiesAndPasswords, _is_valid_puzzle2)