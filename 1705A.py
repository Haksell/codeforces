# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, x = map(int, input().split())
    h = sorted(map(int, input().split()))
    print("YES" if all(h[i] + x <= h[i + n] for i in range(n)) else "NO")
