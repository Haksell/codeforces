# ruff: noqa: E731, E741
def solve(a, d, m, g, p, b):
    if a > g:
        return False
    g -= a
    if d > g + p:
        return False
    x = min(d, g)
    g -= x
    d -= x
    p -= min(d, p)
    return m <= g + p + b


a, d, m = map(int, input().split())
g, p, b = map(int, input().split())
print("YES" if solve(a, d, m, g, p, b) else "NO")
