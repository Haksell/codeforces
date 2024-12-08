# ruff: noqa: E731, E741
for _ in range(int(input())):
    _, l, r, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted([n for n in a if l <= n <= r], reverse=True)
    ans = 0
    while a:
        n = a.pop()
        if n > k:
            break
        k -= n
        ans += 1
    print(ans)
