# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, s, m = map(int, input().split())
    start = 0
    shower = False
    for _ in range(n):
        li, ri = map(int, input().split())
        if li - start >= s:
            shower = True
        start = ri
    print("YES" if shower or m - ri >= s else "NO")
