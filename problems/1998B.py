# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    print(*[pi - 1 or n for pi in p])
