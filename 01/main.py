
import game

def main(values):
    print(game.find3(values))

if __name__ == "__main__":
    # execute only if run as a script
    values = []
    with open('data.txt') as f:
        for line in f:
            values.append(int(line))
    main(values)