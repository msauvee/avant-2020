class Garden:

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __init__(self, lines):
        self._lines = []
        for line in lines:
            filtered_line = ""
            for i in range(0, len(line)):
                if line[i] == '.' or line[i] == '#':
                    filtered_line += line[i]
            if len(filtered_line) > 0:
                self._lines.append(filtered_line)
        self._width = len(self._lines[0])
        self._height = len(self._lines)

    def has_reach_border(self, y):
        return y >= self._height

    def is_tree(self, x, y):
        return self._lines[y][x % self._width] == '#'


def parse(lines):
    return Garden(lines)

def compute(garden, right, down):
    x = y = count = 0
    while not garden.has_reach_border(y):
        count += 1 if garden.is_tree(x, y) else 0
        x += right
        y += down
    return count

def compute_puzzle1(garden):
    return compute(garden, 3, 1)

def compute_puzzle2(garden):
    return compute(garden, 1, 1) * compute(garden, 3, 1) * compute(garden, 5, 1) * compute(garden, 7, 1) * compute(garden, 1, 2)