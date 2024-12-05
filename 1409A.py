# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b = map(int, input().split())
    diff = abs(a - b)
    print(-(-diff // 10))
