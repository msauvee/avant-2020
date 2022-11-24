
import game

def main(values):
    print(f'Result is: {game.compute_puzzle2(values)}')

if __name__ == "__main__":
    # execute only if run as a script
    values = []
    with open('data.txt') as f:
        for line in f:
            values.append(line)
    main(values)