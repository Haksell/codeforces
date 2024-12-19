# ruff: noqa: E731, E741
from collections import deque
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n, k = mir()
        a = deque(sorted(mir()))
        above = n >> 1
        below = (n - 1) >> 1
        r = 0
        for _ in range(k):
            for _ in range(below):
                a.popleft()
            for _ in range(above):
                a.pop()
            r += a.pop()
        print(r)


if __name__ == "__main__":
    main()
