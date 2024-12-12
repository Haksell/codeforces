# ruff: noqa: E731, E741
from itertools import groupby

input()
ans = [
    sum(1 for _ in v)
    for _, v in groupby(x - i for i, x in enumerate(map(int, input().split())))
]
print(len(ans))
print(*ans)
