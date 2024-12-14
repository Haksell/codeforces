# ruff: noqa: E731, E741
h, w = map(int, input().split())
g = [input() for _ in range(h)]
ys = {y for y, r in enumerate(g) if "S" not in r}
xs = {x for x, r in enumerate(zip(*g)) if "S" not in r}
print(sum(y in ys or x in xs for y in range(h) for x in range(w)))
