# ruff: noqa: E731, E741
from bisect import bisect_left
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

MOD = 1_000_000_007


def main():
    for _ in rir():
        read()
        a = sorted(mir())
        b = sorted(mir())
        r = 1
        for i, ai in enumerate(a):
            choices = bisect_left(b, ai) - i
            if choices <= 0:
                r = 0
                break
            r = r * choices % MOD
        print(r)


if __name__ == "__main__":
    main()
