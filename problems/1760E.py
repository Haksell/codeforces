# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(a):
    o = 0
    inv = 0
    for n in a:
        if n == 0:
            inv += o
        else:
            o += 1
    return inv


for _ in rir():
    n = ir()
    a = lmir()
    ans = f(a)
    fz = next((i for i in range(n) if a[i] == 0), None)
    lo = next((i for i in reversed(range(n)) if a[i] == 1), None)
    if fz is not None:
        a[fz] = 1
        ans = max(ans, f(a))
        a[fz] = 0
    if lo is not None:
        a[lo] = 0
        ans = max(ans, f(a))
    print(ans)
