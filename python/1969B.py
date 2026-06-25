# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    s = input()
    r = o = 0
    for c in s:
        if c == "1":
            o += 1
        elif o:
            r += o + 1
    print(r)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
