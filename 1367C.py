# ruff: noqa: E731, E741
from itertools import groupby


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    if all(c == "0" for c in s):
        print((n + k) // (k + 1))
        continue
    groups = [(c, sum(1 for _ in group)) for c, group in groupby(s)]
    ans = 0
    for i, (c, size) in enumerate(groups):
        if c == "0":
            if i in (0, len(groups) - 1):
                ans += size // (k + 1)
            else:
                ans += max(0, (size - k) // (k + 1))
    print(ans)
