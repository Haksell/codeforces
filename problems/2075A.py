# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, k = mir()
    res = 0
    if n & 1:
        res += 1
        n -= k
    k -= 1
    res += (n + k - 1) // k
    print(res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
