# ruff: noqa: E731, E741
n = int(input())
g = [input() for _ in range(n)]
diags = set()
other = set()
for y in range(n):
    for x in range(n):
        (diags if x == y or x == n - y - 1 else other).add(g[y][x])
print("YES" if len(diags) == len(other) == 1 and diags != other else "NO")
