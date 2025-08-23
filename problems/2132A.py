# ruff: noqa: E731, E741
from collections import deque
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    read()
    a = deque(input())
    read()
    b = input()
    c = input()
    for bi, ci in zip(b, c):
        if ci == "V":
            a.appendleft(bi)
        else:
            a.append(bi)
    print("".join(a))


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
