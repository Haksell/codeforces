# ruff: noqa: E731, E741
from copy import deepcopy
import sys

read = sys.stdin.readline
write = sys.stdout.write
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def f(g, m, y, x):
    ans = 0
    for yy, xx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        if 0 <= yy <= 1 and 0 <= xx < m:
            ans += g[yy][xx] == "B"
    return ans


def check(g, m, y, x):
    for xx in range(x, m):
        if g[y][xx] == "W":
            return all(g[yyy][xxx] == "W" for yyy in range(2) for xxx in range(xx, m))
        if g[not y][xx] == "B":
            y = not y
    return True


def is_ham(g, m):
    first_x = next((x for x in range(m) if g[0][x] == "B" or g[1][x] == "B"), None)
    if first_x is None:
        return True
    ans = False
    if g[0][first_x] == "B":
        ans = ans or check(g, m, 0, first_x)
    if g[1][first_x] == "B":
        ans = ans or check(g, m, 1, first_x)
    return ans


def is_con(g, m):
    comp = 0
    for y in range(2):
        for x in range(m):
            if g[y][x] == "W":
                continue
            comp += 1
            stack = [(y, x)]
            while stack:
                y, x = stack.pop()
                for yy, xx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
                    if 0 <= yy <= 1 and 0 <= xx < m and g[yy][xx] == "B":
                        stack.append((yy, xx))
                        g[yy][xx] = "W"
    return comp <= 1


for _ in rir():
    m = ir()
    c1 = read().strip()
    c2 = read().strip()
    g = [list(c1), list(c2)]
    # b = [(y, x) for y in range(2) for x in range(m) if g[y][x] == "B"]
    # l = [f(g, m, y, x) for y, x in b]
    # odds = sum(n & 1 for n in l)
    # print(*g, sep="\n")
    # print(b)
    # print(l, odds)
    # print(_, is_ham(deepcopy(g), m), is_con(deepcopy(g), m))
    print("YES" if is_ham(deepcopy(g), m) else "NO")
