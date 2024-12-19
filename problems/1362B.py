# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(s, i):
    return all(x ^ i in s for x in s)


def main():
    for _ in rir():
        read()
        s = set(mir())
        print(next((i for i in range(1, 1024) if f(s, i)), -1))


if __name__ == "__main__":
    main()
