
import game

def main(values):
    result = game.compute_puzzle1(values)
    print(f'Result to puzzle 1 is: {result}')
    result = game.compute_puzzle2(values)
    print(f'Result to puzzle 2 is: {result}')

if __name__ == "__main__":
    # execute only if run as a script
    values = []
    with open('data.txt') as f:
        for line in f:
            if len(line) == 11:
                values.append(line[0:10])
    main(values)