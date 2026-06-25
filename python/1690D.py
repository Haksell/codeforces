# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ans = w = s[:k].count("W")
    for i in range(k, n):
        w += (s[i] == "W") - (s[i - k] == "W")
        ans = min(ans, w)
    print(ans)
