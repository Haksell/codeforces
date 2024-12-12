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
        read()
        a = lmir()
        res = [a[0]] + list(map(min, a, a[1:])) + [a[-1]]
        print(*res)


if __name__ == "__main__":
    main()
