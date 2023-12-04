import math
import re
from typing import List

from solutions.common import load_data


class Solver:
    NUMBER_FINDER = re.compile(
        r"Card[ ]+(?P<index>\d+): (?P<winning>[\d ]+)\| (?P<mine>[\d ]+)"
    )

    def _parse_input_lines(self, data: List[str]):
        numbers = list(map(lambda x: self.NUMBER_FINDER.match(x), data))

        games = []
        
        for num in numbers:
            winning = list(map(lambda x: int(x), re.findall(r'\d+', num["winning"])))
            mine = list(map(lambda x: int(x), re.findall(r'\d+', num["mine"])))

            game = {
                "index": num["index"],
                "winning": winning,
                "mine": mine
            }

            games.append(game)

        return games

    def solve_part1(self, data: List[str]):
        games = self._parse_input_lines(data)

        total = 0

        for game in games:
            winning_nums = 0
            winning = game['winning']

            for m in game['mine']:
                winning_nums += 1 if m in winning else 0

            if winning_nums > 0:
                total += 2 ** (winning_nums - 1)

        return total

    def solve_part2(self, data: List[str]):
        raise NotImplementedError()


if __name__ == "__main__":
    solver = Solver()
    data = load_data(4)

    result1 = solver.solve_part1(data)
    print(f"Part 1 result is: {result1}")

    result2 = solver.solve_part2(data)
    print(f"Part 2 result is: {result2}")
