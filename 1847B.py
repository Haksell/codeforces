# ruff: noqa: E731, E741
from functools import reduce
from operator import and_
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
        x = reduce(and_, a)
        if n == 1 or x != 0:
            print(1)
            continue
        r = 0
        bw = a[0]
        for i in range(n):
            bw &= a[i]
            if bw == 0:
                r += 1
                if i == n - 1:
                    break
                bw = a[i + 1]
        print(r)


if __name__ == "__main__":
    main()
