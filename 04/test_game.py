import game
import pytest

sample = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in"]

valid_passport_data="ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"

invalid_passports=[
    "eyr:1972 cid:100",
    "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "",
    "iyr:2019",
    "hcl:#602927 eyr:1967 hgt:170cm",
    "ecl:grn pid:012533040 byr:1946",
    "",
    "hcl:dab227 iyr:2012",
    "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "",
    "hgt:59cm ecl:zzz",
    "eyr:2038 hcl:74454a iyr:2023",
    "pid:3556412378 byr:2007"]

valid_passport=[
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
    "hcl:#623a2f",
    "",
    "eyr:2029 ecl:blu cid:129 byr:1989",
    "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "",
    "hcl:#888785",
    "hgt:164cm byr:2001 iyr:2015 cid:88",
    "pid:545766238 ecl:hzl",
    "eyr:2022",
    "",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"]

def test_compute():
    assert game.compute_puzzle1(game.parse_passports(sample)) == 2

def test_compute_invalid():
    assert game.compute_puzzle2(game.parse_passports(invalid_passports)) == 0

def test_compute_valid():
    assert game.compute_puzzle2(game.parse_passports(valid_passport)) == 4

def test_parse():
    passports = game.parse_passports(sample)
    assert len(passports) == 4

def test_parse_invalid_field():
     with pytest.raises(ValueError):
        game.parse_passports(["tot:gry pid:860033327 eyr:2020 hcl:#fffffd"])

def test_valid_byr():
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('byr:1937', 'byr:2002')])) == 1
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('byr:1937', 'byr:2003')])) == 0
    
def test_valid_iyr():
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('iyr:2017', 'iyr:2012')])) == 1
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('iyr:2017', 'iyr:2025')])) == 0

def test_valid_eyr():
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('eyr:2020', 'eyr:2022')])) == 1
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('eyr:2020', 'eyr:2035')])) == 0

def test_valid_hgt():
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('hgt:183cm', 'hgt:60in')])) == 1
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('hgt:183cm', 'hgt:190cm')])) == 1
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('hgt:183cm', 'hgt:190in')])) == 0
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('hgt:183cm', 'hgt:190')])) == 0

def test_valid_hcl():
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('hcl:#fffffd', 'hcl:#123abc')])) == 1
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('hcl:#fffffd', 'hcl:#123abz')])) == 0
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('hcl:#fffffd', 'hcl:123abc')])) == 0

def test_valid_ecl():
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('ecl:gry', 'ecl:brn')])) == 1
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('ecl:gry', 'ecl:wat')])) == 0

def test_valid_pid():
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('pid:860033327', 'pid:000000001')])) == 1
    assert game.compute_puzzle2(game.parse_passports([valid_passport_data.replace('pid:860033327', 'pid:0123456789')])) == 0