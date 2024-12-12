# ruff: noqa: E731, E741
for _ in range(int(input())):
    *a, n = map(int, input().split())
    d = max(a) * 3 - sum(a)
    print("YES" if (n - d) % 3 == 0 and n >= d else "NO")
