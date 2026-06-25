# ruff: noqa: E731, E741
from collections import Counter

for _ in range(int(input())):
    s = input()
    counter = Counter(s)
    once = [c for c, v in counter.items() if v == 1]
    twice = [c for c, v in counter.items() if v == 2]
    print(*once, *twice, *twice, sep="")
