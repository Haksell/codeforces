# ruff: noqa: E731, E741

for _ in range(int(input())):
    n, m = map(int, input().split())
    for _ in range(m):
        input()
    print("YES" if n > m else "NO")
