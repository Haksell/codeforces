# ruff: noqa: E731, E741
from collections import defaultdict
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    d = defaultdict(int)
    for _ in rir():
        s = input()
        if d[s] == 0:
            print("OK")
        else:
            print(f"{s}{d[s]}")
        d[s] += 1


if __name__ == "__main__":
    main()
