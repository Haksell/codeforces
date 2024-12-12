# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(min(n + 1, 1 << min(k, 30)))
