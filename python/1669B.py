# ruff: noqa: E731, E741
from collections import defaultdict

for _ in range(int(input())):
    input()
    dd = defaultdict(int)
    for n in input().split():
        dd[n] += 1
        if dd[n] == 3:
            print(n)
            break
    else:
        print(-1)
