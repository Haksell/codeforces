# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        a = lmir()
        if any(a):
            jump = a.index(1)
            print(*range(1, jump + 1), n + 1, *range(jump + 1, n + 1))
        else:
            print(*range(1, n + 2))


if __name__ == "__main__":
    main()
