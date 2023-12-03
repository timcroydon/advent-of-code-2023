import pytest

from solutions.day2 import Solver

raw1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

raw2 = """TODO"""


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


class TestDay2:
    def test_part_1(self, solver: Solver, data1):
        result = solver.solve_part1(data1)
        assert result == 8

    def test_part_2(self, solver: Solver, data2):
        assert False
