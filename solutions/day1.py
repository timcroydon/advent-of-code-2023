from os import name
import re
from typing import List


def load_data() -> List[str]:
    raw = open("data/day1.txt").read()

    data = raw.splitlines()

    return data


class Solver:
    FIND_DIGITS = re.compile("[\d]")

    def solve(self, data: List[str]):
        total = 0

        for d in data:
            digits = self.FIND_DIGITS.findall(d)
            value = int(f"{digits[0]}{digits[-1]}")

            total += value

        return total


if __name__ == "__main__":
    solver = Solver()
    data = load_data()

    result = solver.solve(data)
    print(f"Result is: {result}")
