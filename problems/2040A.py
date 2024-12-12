# ruff: noqa: E731, E741
from collections import defaultdict
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        _, k = mir()
        a = lmir()
        f = randint(1, 1 << 30)
        d = defaultdict(list)
        for i, ai in enumerate(a):
            d[ai % k + f].append(i)
        for k, v in d.items():
            if len(v) == 1:
                print("YES")
                print(v[0] + 1)
                break
        else:
            print("NO")


if __name__ == "__main__":
    main()
