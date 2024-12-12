# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve3(n):
    if n & 3 == 0:
        return [n >> 1, n >> 2, n >> 2]
    mul = 1
    if n & 1 == 0:
        n >>= 1
        mul = 2
    big = (n >> 1) * mul
    return [big, big, mul]


def main():
    for _ in rir():
        n, k = mir()
        res = solve3(n - (k - 3))
        for _ in range(k - 3):
            res.append(1)
        print(*res)


if __name__ == "__main__":
    main()
