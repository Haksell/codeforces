# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))

TRIPLETS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def win(g, player):
    return any(all(g[i] == player for i in triplet) for triplet in TRIPLETS)


def main():
    g = input() + input() + input()
    x, o = sum(r.count("X") for r in g), sum(r.count("0") for r in g)
    d = x - o
    win_o, win_x = win(g, "0"), win(g, "X")
    print(
        "illegal"
        if d not in (0, 1) or (win_x and d == 0) or (win_o and d == 1)
        else "the first player won"
        if win_x
        else "the second player won"
        if win_o
        else "draw"
        if x + o == 9
        else "first"
        if d == 0
        else "second"
    )


if __name__ == "__main__":
    main()
