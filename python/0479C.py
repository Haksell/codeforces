# ruff: noqa: E731, E741
n = int(input())
l = sorted([list(map(int, input().split())) for _ in range(n)])
res = 0
for a, b in l:
    res = b if b >= res else a
print(res)
