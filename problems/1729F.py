# ruff: noqa: E731, E741
from itertools import accumulate, product
from math import inf
import sys

sys.setrecursionlimit(25000)
cin = sys.stdin
read = cin.readline
cout = sys.stdout
write = cout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

for _ in rir():
    s = list(map(int, read().strip()))
    a = [0] + list(accumulate(s))
    w, m = mir()
    mod = sum(s[:w])
    mods = [mod % 9]
    for i in range(w, len(s)):
        mod += s[i] - s[i - w]
        mods.append(mod % 9)
    imods = [[] for _ in range(9)]
    for i, mod in enumerate(mods):
        imods[mod].append(i)
    for _ in range(m):
        l, r, k = mir()
        m = (a[r] - a[l - 1]) % 9
        sol = (inf, inf)
        for i, j in product(range(9), repeat=2):
            if (i * m + j) % 9 == k:
                if i == j:
                    if len(imods[i]) >= 2:
                        sol = min(sol, (imods[i][0], imods[i][1]))
                else:
                    if imods[i] and imods[j]:
                        sol = min(sol, (imods[i][0], imods[j][0]))

        if sol != (inf, inf):
            print(sol[0] + 1, sol[1] + 1)
        else:
            print(-1, -1)
