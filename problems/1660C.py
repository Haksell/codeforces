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
        s = input()
        pos = [deque() for _ in range(26)]
        for i, c in enumerate(s):
            pos[ord(c) - 97].append(i)
        i = 0
        r = len(s)
        while True:
            m = len(s)
            for d in pos:
                while d and d[0] < i:
                    d.popleft()
                if len(d) >= 2:
                    m = min(m, d[1])
            if m < len(s):
                r -= 2
                i = m + 1
            else:
                break
        print(r)


if __name__ == "__main__":
    main()
