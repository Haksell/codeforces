# ruff: noqa: E731, E741
from collections import Counter
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def handshake(n):
    return n * (n - 1) >> 1


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        s = sum(a)
        d, m = divmod(s, n)
        if m == 0:
            target = d << 1
        elif 2 * m == n:
            target = d << 1 | 1
        else:
            print(0)
            continue
        c = Counter(a)
        diff = sum(v * c[target - k] for k, v in c.items() if 2 * k != target) >> 1
        print(diff + handshake(c[d]) if m == 0 else diff)


if __name__ == "__main__":
    main()
