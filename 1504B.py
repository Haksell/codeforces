# ruff: noqa: E731, E741
from collections import Counter
from itertools import accumulate


def g(n, a, b):
    if a.count("1") != b.count("1"):
        return False

    if n & 1:
        if a[-1] != b[-1]:
            return False
        n -= 1
        a = a[:-1]
        b = b[:-1]

    ca = Counter("".join(sorted(a[i : i + 2])) for i in range(0, n, 2))
    cb = Counter("".join(sorted(b[i : i + 2])) for i in range(0, n, 2))
    if ca != cb:
        return False

    idx = {
        i for i, x in enumerate(accumulate(1 if d == "0" else -1 for d in a)) if x == 0
    }
    swap = True
    for i in range(n - 1, -1, -1):
        if (a[i] != b[i]) == swap:
            if i in idx:
                swap = not swap
            else:
                return False
    return True


for _ in range(int(input())):
    print("YES" if g(int(input()), input(), input()) else "NO")
