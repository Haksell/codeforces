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
        x, y, n = mir()
        res = [0] * n
        res[-1] = y
        for i in range(1, n):
            res[~i] = res[-i] - i
        if res[0] < x:
            print(-1)
        else:
            res[0] = x
            print(*res)


if __name__ == "__main__":
    main()
