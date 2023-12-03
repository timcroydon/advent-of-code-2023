import re
from typing import List

from solutions.common import load_data


class Solver:
    FIND_DIGITS = re.compile(r"(\d)")
    # include lookahead (?=) to capture overlapping matches
    FIND_DIGITS_AND_WORDS = re.compile(
        r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    )

    DIGIT_MAP = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    def _word_to_number(self, digit):
        if digit in self.DIGIT_MAP:
            return self.DIGIT_MAP.index(digit)
        else:
            return digit

    def _find_digits(self, finder: re, data: List[str]):
        total = 0

        for d in data:
            digits = finder.findall(d)

            first = self._word_to_number(digits[0])
            last = self._word_to_number(digits[-1])

            value = int(f"{first}{last}")

            total += value

        return total

    def solve_part1(self, data: List[str]):
        result = self._find_digits(self.FIND_DIGITS, data)

        return result

    def solve_part2(self, data: List[str]):
        result = self._find_digits(self.FIND_DIGITS_AND_WORDS, data)

        return result


if __name__ == "__main__":
    solver = Solver()
    data = load_data(1)

    result1 = solver.solve_part1(data)
    result2 = solver.solve_part2(data)

    print(f"Part 1 result is: {result1}")
    print(f"Part 2 result is: {result2}")
