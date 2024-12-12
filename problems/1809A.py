# ruff: noqa: E731, E741
from collections import Counter


for _ in range(int(input())):
    partition = sorted(Counter(input()).values())
    match partition:
        case [4]:
            print(-1)
        case [1, 3]:
            print(6)
        case _:
            print(4)
