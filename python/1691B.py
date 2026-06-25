# ruff: noqa: E731, E741
from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    d = defaultdict(list)
    for i, si in enumerate(s, 1):
        d[si].append(i)
    if any(len(idxs) == 1 for idxs in d.values()):
        print(-1)
    else:
        ans = [0] * (n)
        for idxs in d.values():
            for i, j in zip(idxs, idxs[1:] + [idxs[0]]):
                ans[i - 1] = j
        print(*ans)
