import game

def main(values):
    result = game.compute_puzzle1(25, values)
    print(f'Result to puzzle 1 is: {result}')
    result = game.compute_puzzle2(25, values)
    print(f'Result to puzzle 2 is: {result}')

if __name__ == "__main__":
    # execute only if run as a script
    values = []
    with open('data.txt') as f:
        for line in f:
            if line[-1:] == '\n':
                line = line[:-1]
            if len(line) > 0:
                values.append(int(line))
    main(values)