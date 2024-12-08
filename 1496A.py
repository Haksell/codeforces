# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    m = 2 * k + 1
    print("NO" if m > n else "YES" if s[:k] == s[n - k :][::-1] else "NO")
