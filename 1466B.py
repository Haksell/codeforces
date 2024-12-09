# ruff: noqa: E731, E741
from math import inf

for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    ans = 0
    last = inf
    for note in reversed(x):
        if note != last:
            ans += 1
            last = note if note + 1 == last else note + 1
    print(ans)
