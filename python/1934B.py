# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

COINS = [1, 3, 6, 10, 15]
DP_SIZE = 60
RESTS = [1 << 30] * DP_SIZE
RESTS[0] = 0
for i in range(1, DP_SIZE):
    for c in COINS:
        if c > i:
            continue
        RESTS[i] = min(RESTS[i], RESTS[i - c] + 1)


def solve():
    n = ir()
    q, r = divmod(n, 15)
    m = min(q, 3)
    r += 15 * m
    print(q - m + RESTS[r])


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
