# ruff: noqa: E731, E741
from collections import deque
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    f = randint(1, 1 << 30)
    n, k = mir()
    a = lmir()
    s = set()
    d = deque()
    for x in a:
        if x + f in s:
            continue
        if len(d) == k:
            s.discard(d.popleft() + f)
        d.append(x)
        s.add(x + f)
    print(len(d))
    print(*reversed(d))


if __name__ == "__main__":
    main()
