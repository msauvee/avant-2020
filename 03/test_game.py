import game

def test_compute():
    garden = game.parse([
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#"])
    assert game.compute(garden, 3, 1) == 7

def test_filter_carriage_return_and_empty_lines():
    garden = game.parse(["..#\n\n"])
    assert garden.width == 3
    assert garden.height == 1

    