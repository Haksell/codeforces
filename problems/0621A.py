# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    read()
    a = lmir()
    s = sum(a)
    print(s - min(ai for ai in a if ai & 1) if s & 1 else s)


if __name__ == "__main__":
    main()
