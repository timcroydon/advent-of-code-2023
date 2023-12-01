import pytest

from solutions.day1 import Solver


raw = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


@pytest.fixture(scope="module")
def solver():
    return Solver()


@pytest.fixture(scope="module")
def data():
    data = raw.splitlines()

    return data


class TestDay1:
    def test_day_1(self, solver, data):
        result = solver.solve(data)
        assert result == 142
