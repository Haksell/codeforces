# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def solve():
    n, m = mir()
    cards = [lmir() for _ in range(n)]
    res = 0
    for x in range(m):
        values = sorted(card[x] for card in cards)
        total = 0
        for i, v in enumerate(values):
            res += v * i - total
            total += v
    print(res)


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
