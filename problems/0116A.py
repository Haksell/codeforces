# ruff: noqa: E731, E741
inside = 0
res = 0
for _ in range(int(input())):
    down, up = map(int, input().split())
    inside += up - down
    res = max(res, inside)
print(res)
