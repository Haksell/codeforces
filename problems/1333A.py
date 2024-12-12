# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, w = map(int, input().split())
    print("B" * w)
    for _ in range(h - 1):
        print("B" + "W" * (w - 1))
