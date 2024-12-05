# ruff: noqa: E731, E741
for _ in range(int(input())):
    _, y = map(int, input().split())
    print("YES" if y >= -1 else "NO")
