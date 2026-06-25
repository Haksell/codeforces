# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = sorted(a)
    r = {x: i for i, x in enumerate(s)}
    z = sum(r[y] == r[x] + 1 for x, y in zip(a, a[1:]))
    print("YES" if z + k >= n else "NO")
