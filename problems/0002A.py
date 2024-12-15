# ruff: noqa: E731, E741
from collections import defaultdict
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    lines = []
    d = defaultdict(int)
    for _ in rir():
        player, n = input().split()
        n = int(n)
        lines.append((player, n))
        d[player] += n
    max_score = max(d.values())
    winners = {k for k, v in d.items() if v == max_score}
    d = defaultdict(int)
    for player, n in lines:
        if player not in winners:
            continue
        d[player] += n
        if d[player] >= max_score:
            print(player)
            return


if __name__ == "__main__":
    main()
