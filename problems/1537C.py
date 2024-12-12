# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    h = sorted(map(int, input().split()))
    if len(h) == 2:
        print(*h)
    else:
        i = min(range(1, n), key=lambda i: h[i] - h[i - 1])
        print(*h[i:], *h[:i])
