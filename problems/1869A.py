# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        n = ir()
        read()
        ops = [(1, n)]
        if n & 1:
            ops.append((1, n - 1))
            ops.append((n - 1, n))
            ops.append((n - 1, n))
        else:
            ops.append((1, n))
        print(len(ops))
        for lo, hi in ops:
            print(lo, hi)


if __name__ == "__main__":
    main()
