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
        a.sort()
        dx = a[n - 1] - a[0]
        dy = a[2 * n - 1] - a[n]
        print(dx + dy)
        for i in range(n):
            print(a[i], a[~i])


if __name__ == "__main__":
    main()
