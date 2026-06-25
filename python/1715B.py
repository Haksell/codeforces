# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve(n, k, b, s):
    rem = s - k * b
    if 0 <= rem <= n * (k - 1):
        res = [0] * n
        res[0] = k * b
        for i in range(n):
            res[i] += min(rem, k - 1)
            rem -= k - 1
            if rem <= 0:
                break
        return res
    else:
        return [-1]


def main():
    for _ in rir():
        n, k, b, s = mir()
        print(*solve(n, k, b, s))


if __name__ == "__main__":
    main()
