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
        n, x, y = mir()
        if x == y == 0 or x != 0 and y != 0:
            print(-1)
            continue
        m = x or y
        if (n - 1) % m != 0:
            print(-1)
            continue
        print(*[i // m * m + 2 for i in range(n - 1)])


if __name__ == "__main__":
    main()
