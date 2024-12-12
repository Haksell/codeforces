# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    if 2 * k >= n:
        print(-1)
        continue
    ans = [0] * n
    for i in range(k):
        ans[2 * i + 1] = n - i
    x = n - k
    for i in range(n):
        if ans[i] == 0:
            ans[i] = x
            x -= 1
    print(*ans)
