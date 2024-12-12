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
        n, m = mir()
        res = 0
        for _ in range(n):
            m -= len(input())
            res += m >= 0
        print(res)


if __name__ == "__main__":
    main()