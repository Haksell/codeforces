# ruff: noqa: E731, E741
input()
a = []
m = 0
for b in map(int, input().split()):
    a.append(m + b)
    if b > 0:
        m += b
print(*a)
