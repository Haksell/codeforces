# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, s, r = map(int, input().split())
    m = s - r
    ans = [1] * n
    ans[0] = m
    s -= n + m - 1
    for i in range(1, n):
        change = min(m - 1, s)
        ans[i] += change
        s -= change
        if s == 0:
            break
    print(*ans)
