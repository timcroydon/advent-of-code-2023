from typing import List

from solutions.common import load_data


class Solver:
    RED = 12
    GREEN = 13
    BLUE = 14

    def _parse_game(self, game: str):
        x = game.removeprefix("Game ").split(":")
        index = int(x[0])

        rounds = x[1].split(";")

        cubes = {"red": [], "green": [], "blue": []}

        for i, r in enumerate(rounds):
            colour_total = r.split(",")

            # assume don't get repeats of each colour in each round
            for s in colour_total:
                value = s.strip().split()
                cubes[value[1]].append(int(value[0]))

            red_max = max(cubes["red"]) if len(cubes["red"]) else 0
            green_max = max(cubes["green"]) if len(cubes["green"]) else 0
            blue_max = max(cubes["blue"]) if len(cubes["blue"]) else 0

        if red_max > self.RED or green_max > self.GREEN or blue_max > self.BLUE:
            return 0
        else:
            return index

    def solve_part1(self, data: List[str]):
        total = 0

        for game in data:
            total += self._parse_game(game)

        return total

    def solve_part2(self, data: List[str]):
        raise NotImplementedError()


if __name__ == "__main__":
    solver = Solver()
    data = load_data(2)

    result1 = solver.solve_part1(data)
    print(f"Part 1 result is: {result1}")

    result2 = solver.solve_part2(data)
    print(f"Part 2 result is: {result2}")
