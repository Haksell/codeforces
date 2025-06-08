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
    a = input()
    z = a.count("0")
    o = n - z
    max_good = o // 2 + z // 2
    min_good = n // 2 - min(o, z)
    print("YES" if min_good <= k <= max_good and (k - min_good) & 1 == 0 else "NO")


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
