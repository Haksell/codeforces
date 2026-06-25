# ruff: noqa: E731, E741
from itertools import count
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def is_fair(n):
    m = n
    while m > 0:
        m, d = divmod(m, 10)
        if d and n % d != 0:
            return False
    return True


def main():
    for _ in rir():
        print(next(n for n in count(ir()) if is_fair(n)))


if __name__ == "__main__":
    main()
