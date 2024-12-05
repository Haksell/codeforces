# ruff: noqa: E731, E741
from itertools import groupby


for _ in range(int(input())):
    input()
    print(
        max(
            (sum(1 for _ in v) for k, v in groupby(input().split()) if k == "0"),
            default=0,
        )
    )
