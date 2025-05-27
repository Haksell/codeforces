# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    read()
    cnt = [3, 1, 2, 1, 0, 1, 0, 0, 0, 0]
    nz = 5
    for i, n in enumerate(mir()):
        cnt[n] -= 1
        nz -= cnt[n] == 0
        if nz == 0:
            return i + 1
    return 0


def main():
    for _ in rir():
        print(solve())


if __name__ == "__main__":
    main()
