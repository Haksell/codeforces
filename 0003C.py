# ruff: noqa: E731, E741
def triplets(g):
    for r in g:
        yield r
    for c in zip(*g):
        yield "".join(c)
    yield "".join(r[i] for i, r in enumerate(g))
    yield "".join(r[~i] for i, r in enumerate(g))


def win(g, player):
    target = 3 * player
    return any(map(target.__eq__, triplets(g)))


def solve(g):
    x, o = sum(r.count("X") for r in g), sum(r.count("0") for r in g)
    d = x - o
    win_o, win_x = win(g, "0"), win(g, "X")
    return (
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


print(solve(g=[input() for _ in range(3)]))
