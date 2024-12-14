# ruff: noqa: E731, E741
n, x = map(int, input().split())
res = 0
for _ in range(n):
    op, d = input().split()
    d = int(d)
    if op == "+":
        x += d
    elif x >= d:
        x -= d
    else:
        res += 1
print(x, res)
