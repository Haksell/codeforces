# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    x = sorted(map(int, input().split()))
    ans = 0
    t = n - 1
    while x:
        d = n - x.pop()
        if d > t:
            break
        ans += 1
        t -= d
    print(ans)
