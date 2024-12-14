# ruff: noqa: E731, E741
from copy import deepcopy


def dfs(m, w, h):
    m = deepcopy(m)
    x, y = next((x, y) for x in range(w) for y in range(h) if m[y][x] == ".")
    ans = [(x, y)]
    stack = [(x, y)]
    m[y][x] = "#"
    while stack:
        x, y = stack.pop()
        for nx, ny in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
            if 0 <= nx < w and 0 <= ny < h and m[ny][nx] == ".":
                stack.append((nx, ny))
                ans.append((nx, ny))
                m[ny][nx] = "#"
    return ans[::-1]


h, w, k = map(int, input().split())
m = [list(input()) for _ in range(h)]
for x, y in dfs(m, w, h)[:k]:
    m[y][x] = "X"
for row in m:
    print("".join(row))

"""
12 12 6
..##########
...#########
##..########
##...#######
####..######
####...#####
######..####
######...###
########..##
########...#
##########..
##########..

10 10 15
..########
...#######
#...######
##...#####
###...####
####...###
#####...##
######...#
#######...
########..

10 10 5
..........
.#######..
.#########
.#########
.#########
.#########
.#########
.#########
.#######..
..........

5 5 5
.....
.....
.....
.....
.....

10 10 3
..........
.########.
.####..##.
.####.....
.#########
.#########
.####.....
.####..##.
.########.
..........

10 10 3
..........
.########.
.#..#..##.
.#........
.#########
.#########
.#........
.#..#..##.
.########.
..........

7 7 18
#.....#
..#.#..
.#...#.
...#...
.#...#.
..#.#..
#.....#

10 10 3
#.########
..........
#.#######.
#.#######.
#.#######.
#.#######.
#.#######.
#.#######.
#.#######.
#.........
"""
