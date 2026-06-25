# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        while a[i] > n:
            a[i] >>= 1
    a.sort(reverse=True)
    s = set()
    for i in range(n):
        while a[i] > 0 and a[i] in s:
            a[i] >>= 1
        s.add(a[i])
    print("YES" if sorted(a) == list(range(1, n + 1)) else "NO")
