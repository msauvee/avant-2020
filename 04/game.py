import re

class Passport:

    def add_datas(self, datas):
        for data in datas:
            if len(data)=='' or ':' not in data:
                continue
            field=data.split(':')[0]
            value=data.split(':')[1]
            if field not in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']:
                raise ValueError(f'invalid field {field}')
            self._data[field] = value

    def __init__(self):
        self._data = {}

    def is_valid_puzzle1(self):
        return len(self._data.keys()) == 8 or (len(self._data.keys()) == 7 and 'cid' not in self._data)

    def is_valid_puzzle2(self):
        if not self.is_valid_puzzle1():
            return False
        if len(self._data['byr']) != 4 or int(self._data['byr']) < 1920 or int(self._data['byr']) > 2002:
            return False 
        if len(self._data['iyr']) != 4 or int(self._data['iyr']) < 2010 or int(self._data['iyr']) > 2020:
            return False 
        if len(self._data['eyr']) != 4 or int(self._data['eyr']) < 2020 or int(self._data['eyr']) > 2030:
            return False 
        if len(self._data['hgt']) <= 2:
            return False
        if self._data['hgt'][-2:] == 'in':
            if int(self._data['hgt'][:-2]) < 59 or int(self._data['hgt'][:-2]) > 76:
                return False
        elif self._data['hgt'][-2:] == 'cm':
            if int(self._data['hgt'][:-2]) < 150 or int(self._data['hgt'][:-2]) > 193:
                return False
        else:
            return False
        pattern_hcl = re.compile(r'^#([0-9|a-f]){6}$')    
        if pattern_hcl.match(self._data['hcl']) is None:
            return False
        if self._data['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        pattern_pid = re.compile(r'^[0-9]{9}$')    
        if pattern_pid.match(self._data['pid']) is None:
            return False
        return True

def parse_passports(lines):
    passports=[]
    current_passport = None
    for line in lines:
        if len(line.strip()) == 0 and not current_passport is None:
            current_passport =  None
        if current_passport is None:
            current_passport = Passport()
            passports.append(current_passport)
        current_passport.add_datas(line.strip().split(' '))       
    return passports

def compute_puzzle1(passports):
    count = 0
    for passport in passports:
        count += 1 if passport.is_valid_puzzle1() else 0 
    return count

def compute_puzzle2(passports):
    count = 0
    for passport in passports:
        count += 1 if passport.is_valid_puzzle2() else 0 
    return count