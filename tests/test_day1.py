import pytest

from solutions.day1 import Solver


raw1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

raw2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


@pytest.fixture(scope="module")
def solver():
    return Solver()


@pytest.fixture(scope="module")
def data1():
    data = raw1.splitlines()

    return data


@pytest.fixture(scope="module")
def data2():
    data = raw2.splitlines()

    return data


class TestDay1:
    def test_part_1(self, solver: Solver, data1):
        result = solver.solve_part1(data1)
        assert result == 142

    def test_part_2(self, solver: Solver, data2):
        result = solver.solve_part2(data2)
        assert result == 281

    @pytest.mark.parametrize(
        "input, expected",
        [
            ("zero", 0),
            ("one", 1),
            ("two", 2),
            ("three", 3),
            ("four", 4),
            ("five", 5),
            ("six", 6),
            ("seven", 7),
            ("eight", 8),
            ("nine", 9),
            ("0", 0),
            ("1", 1),
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
        ],
    )
    def test_word_to_number(self, solver, input, expected):
        result = solver._word_to_number(input)

        assert int(result) == expected
