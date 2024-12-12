# ruff: noqa: E731, E741
from itertools import accumulate, count
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


for _ in rir():
    n, c, d = mir()
    a = sorted(lmir(), reverse=True)
    acc = [0] + list(accumulate(a))
    m = a[0]
    s = acc[-1]
    if sum(a[:d]) >= c:
        print("Infinity")
    elif m * d < c:
        print("Impossible")
    elif d // n * s + acc[d % n] >= c:
        guess = d * c // s + 1
        for k in count(guess, -1):
            if d // k * s + acc[min(d % k, n)] >= c:
                print(k - 1)
                break
    else:
        for k in range(n - 1, -1, -1):
            full = acc[k + 1]
            part = acc[d % (k + 1)]
            gain = full * (d // (k + 1)) + part
            if gain >= c:
                print(k)
                break
