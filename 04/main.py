import game

def main(values):
    passports = game.parse_passports(values)
    result = game.compute_puzzle1(passports)
    print(f'Result to puzzle 1 is: {result}')
    result = game.compute_puzzle2(passports)
    print(f'Result to puzzle 2 is: {result}')

if __name__ == "__main__":
    # execute only if run as a script
    values = []
    with open('data.txt') as f:
        for line in f:
            values.append(line)
    main(values)