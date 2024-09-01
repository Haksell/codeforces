from collections import Counter
from itertools import islice
import sys

read = sys.stdin.readline
write = sys.stdout.write
input = lambda: read().strip()  # noqa: E731
ir = lambda: int(read())  # noqa: E731
rir = lambda: range(int(read()))  # noqa: E731
mir = lambda: map(int, read().split())  # noqa: E731
lmir = lambda: list(map(int, read().split()))  # noqa: E731


def counts(a):
    res = [0] * 26
    for ai in a:
        res[ai] += 1
    return res


for _ in rir():
    n = ir()
    s = input()
    if n == 1:
        print(1)
    elif n & 1:
        s = [ord(c) - 97 for c in s]
        c0 = counts(s[1::2])
        c1 = counts(s[2::2])
        m0 = max(c0)
        m1 = max(c1)
        res = cur = n - m0 - m1
        for i, (cl, cr) in enumerate(zip(s, islice(s, 1, None))):
            if i & 1 == 0:
                c0[cl] += 1
                m0 = max(m0, c0[cl])
                c0[cr] -= 1
                if c0[cr] + 1 == m0:
                    m0 = max(c0)
            else:
                c1[cl] += 1
                m1 = max(m1, c1[cl])
                c1[cr] -= 1
                if c1[cr] + 1 == m1:
                    m1 = max(c1)
            cur = n - m0 - m1
            res = min(res, cur)
        print(res)
    else:
        c0 = Counter(s[0::2])
        c1 = Counter(s[1::2])
        print(n - c0.most_common(1)[0][1] - c1.most_common(1)[0][1])
