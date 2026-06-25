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
        a = deque(mir())
        while k >= 2 and len(a) >= 2:
            m = min(a[0], a[-1], k >> 1)
            if a[0] == m:
                a.popleft()
            else:
                a[0] -= m
            if a[-1] == m:
                a.pop()
            else:
                a[-1] -= m
            k -= 2 * m
        if k == 1 and a and a[0] == 1:
            a.popleft()
            k -= 1
        elif len(a) == 1 and a[0] <= k:
            a.popleft()
        print(n - len(a))


if __name__ == "__main__":
    main()
