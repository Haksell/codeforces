# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    o = sum(int(x) & 1 for x in input().split())
    print(min(o, n - o))
