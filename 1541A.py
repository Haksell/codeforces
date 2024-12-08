# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    l = [(x ^ 1) + 1 for x in range(n)]
    if n & 1:
        l[-3] += 1
        l[-1] -= 2
    print(*l)
