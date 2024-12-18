# ruff: noqa: E731, E741
from functools import reduce
from operator import xor
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        x = reduce(xor, a)
        if x == 0:
            print("YES")
        else:
            y = 0
            cnt = 0
            for i in range(n - 1):
                y ^= a[i]
                if y == x:
                    y = 0
                    cnt += 1
            print("YES" if cnt >= 2 else "NO")


if __name__ == "__main__":
    main()
