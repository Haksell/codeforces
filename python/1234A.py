# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = sum(map(int, input().split()))
    print(-(-s // n))
