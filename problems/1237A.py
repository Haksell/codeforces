# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    up = True
    for _ in rir():
        n = ir()
        if n % 2 == 0:
            print(n // 2)
        else:
            print((n + up) // 2)
            up = not up


if __name__ == "__main__":
    main()
