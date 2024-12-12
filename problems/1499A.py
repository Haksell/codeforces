# ruff: noqa: E731, E741
for _ in range(int(input())):
    n, k1, k2 = map(int, input().split())
    w, b = map(int, input().split())
    white = k1 + k2
    black = n + n - k1 - k2
    print("YES" if white >= 2 * w and black >= 2 * b else "NO")
