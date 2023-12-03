from typing import List


def load_data(day: int) -> List[str]:
    raw = open(f"data/day{day}.txt").read()

    data = raw.splitlines()

    return data
