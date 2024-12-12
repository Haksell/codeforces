# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    x, y = divmod(n - 1, h)
    print(y * w + x + 1)
