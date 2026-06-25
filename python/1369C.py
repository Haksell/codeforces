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
        w = sorted(mir(), reverse=True)
        r = 0
        while w and w[-1] == 1:
            r += a.pop() << 1
            w.pop()
        for wi in w:
            r += a.pop() + a.popleft()
            for _ in range(wi - 2):
                a.popleft()
        print(r)


if __name__ == "__main__":
    main()
