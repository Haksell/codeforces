# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(s, k):
    if k > len(s):
        return 0
    d = [0] * 10
    for i in range(k):
        d[s[i]] += 1
    z = 10 - d.count(0)
    m = max(d)
    res = max(d) <= z
    for i in range(k, len(s)):
        d[s[i]] += 1
        d[s[i - k]] -= 1
        if s[i] != s[i - k]:
            z += (d[s[i]] == 1) - (d[s[i - k]] == 0)
            if d[s[i]] == m + 1:
                m += 1
            elif d[s[i - k]] == m - 1:
                m = max(d)
        res += m <= z
    return res


for _ in rir():
    n = ir()
    s = list(map(int, read().strip()))
    print(sum(f(s, k) for k in range(1, 101)))
