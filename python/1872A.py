# ruff: noqa: E731, E741
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(-(-abs(a - b) // (c << 1)))
