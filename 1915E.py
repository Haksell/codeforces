# ruff: noqa: E731, E741
from random import randint
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(a):
    acc = randint(1, 1 << 30)
    seen = {acc}
    for i, ai in enumerate(a):
        acc += -ai if i & 1 else ai
        if acc in seen:
            return True
        seen.add(acc)
    return False


def main():
    for _ in rir():
        read()
        print("YES" if solve(lmir()) else "NO")


if __name__ == "__main__":
    main()
