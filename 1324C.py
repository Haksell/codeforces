# ruff: noqa: E731, E741
from itertools import groupby

for _ in range(int(input())):
    print(
        1 + max((sum(1 for _ in v) for k, v in groupby(input()) if k == "L"), default=0)
    )
