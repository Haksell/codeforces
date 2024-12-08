# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)
    ans = a[-1]
    removed = 0
    while len(a) >= 2:
        x = a.pop()
        removed += x - removed
        ans = max(ans, a[-1] - removed)
    print(ans)
