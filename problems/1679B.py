# ruff: noqa: E731, E741
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    f = randint(1 << 29, 1 << 30)
    n, q = mir()
    a = lmir()
    vals = {i + f: ai for i, ai in enumerate(a)}
    default = 0
    s = sum(a)
    for _ in range(q):
        query, *maybe_i, val = lmir()
        if query == 1:
            i = maybe_i[0] - 1 + f
            s += val - vals.get(i, 0)
            vals[i] = val
        else:
            vals.clear()
            default = val
            s = 0
        print(s + (n - len(vals)) * default)


if __name__ == "__main__":
    main()
