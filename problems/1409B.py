# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, x, y, n = map(int, input().split())
    aa = max(x, a - n)
    bb = max(y, b - n)
    print(aa * max(y, b + a - n - aa) if aa < bb else bb * max(x, b + a - n - bb))
